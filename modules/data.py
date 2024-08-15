import asyncio

import aiohttp
import pandas as pd

from agents.resume import resume_conv_raw_to_md
from agents.resume import resume_conv_md_to_json
from agents.resume import resume_section_info
from agents.resume import resume_section_templates
from configs.categories import category_keymap

from gpt import OpenAI
from tools import Files, Ledger
from modules.glassdoor import Glassdoor
from builders import ResumeBuilder


class Data:
    def __init__(
            self,
            user_name: str,
            platform: str,
            renew_categories: bool = False,
            renew_descriptions: bool = False,
    ):
        self._renew_categories = renew_categories

        self.ledger = Ledger().data(user_name, platform)
        self.paths = self.ledger["paths"]
        self.files = Files()

        self.biography = self.files.read_file(self.paths["files"]["biography"], default="")
        self.preferences = self.files.read_json(self.paths["files"]["preferences"], default={})
        self.resume_raw = self.files.read_file(self.paths["files"]["resume"]["raw"], default="")
        self.resume_md = self.files.read_json(self.paths["files"]["resume"]["md"], default={})
        self.resume_text = self.files.read_file(self.paths["files"]["resume"]["text"], default="")
        self.resume_json = self.files.read_json(self.paths["files"]["resume"]["json"], default={})
        self.resume_repl = self.files.read_file(self.paths["files"]["resume"]["repl"], default="")
        self.jobs_list = self.fetch_jobs_list(platform=platform, renew=renew_descriptions)
        self.categories = None

    async def prepare_data(self):
        if self.resume_repl != self.resume_raw:
            completions_model = OpenAI(self.ledger["models"]["completions"])
            async with aiohttp.ClientSession() as session:
                await self.resume_to_md(completions_model, session)
                await self.resume_to_json(completions_model, session)
            self.resume_repl = self.resume_raw

            self.files.write_json(self.paths["files"]["resume"]["md"], self.resume_md)
            self.files.write_json(self.paths["files"]["resume"]["json"], self.resume_json)
            self.files.write_file(self.paths["files"]["resume"]["text"], self.resume_text)
            self.files.write_file(self.paths["files"]["resume"]["repl"], self.resume_repl)

            ResumeBuilder().build(
                data=self.resume_json,
                path=self.paths["dirs"]["resume"],
                file_name="resume",
                del_tmp_files=False,
                include_summary=False,
                hyperlink_decorations=False)
        await self.load_categories()

    async def resume_to_md(self, openai_client: OpenAI, session: aiohttp.ClientSession):
        """
        Convert raw resume to MarkDown format.

        :return: Tuple of resume markdown and log.
        """
        context = resume_conv_raw_to_md
        content = f"&&&{self.resume_raw}&&&"
        context = [
            {"content": context, "role": "system"},
            {"content": content, "role": "user"}
        ]

        response = await openai_client.get_response(
            context=context,
            response_format="json_object",
            session=session)
        self.resume_md = response["output"]
        if {"info", "work", "project", "education", "skills", "certifications", "others"} - self.resume_md.keys():
            return await self.resume_to_md(openai_client, session)
        self.resume_text = "\n\n".join(self.resume_md.values())

    async def resume_to_json(self, openai_client: OpenAI, session: aiohttp.ClientSession):
        """
        Convert resume markdown to JSON format.

        :return: Tuple of resume JSON and logs.
        """

        async def get_section_json(section, content, backoff=1):
            context = resume_conv_md_to_json.format(
                template_info=resume_section_info[section],
                template=resume_section_templates[section],
                section=section)
            content = f"CONTENTS OF THE {section} SECTION OF THE CV: \n&&&{content}&&&"
            context = [
                {"content": context, "role": "system"},
                {"content": content, "role": "user"}
            ]

            response = await openai_client.get_response(
                context=context,
                response_format="json_object",
                session=session)
            completion = response["output"]
            if isinstance(completion, dict) and len(completion) == 1:
                return section, completion.get(section, completion)
            else:
                await asyncio.sleep(backoff)
                return await get_section_json(section, content, backoff=backoff * 2)

        md_to_json_tasks = [
            get_section_json(section=key, content=value)
            for key, value in self.resume_md.items()
            if value != ""
        ]
        sections_json = await asyncio.gather(*md_to_json_tasks)
        self.resume_json = {key: value for key, value in sections_json}

    async def load_categories(self):
        async def get_embedding(category: str, definition: str, keywords: str) -> dict:
            """
            Get embeddings for category definition and keywords.

            :param category: Category name.
            :param definition: Category definition.
            :param keywords: Category keywords.
            :return: Dictionary with category embeddings.
            """
            context = f"{category}: {definition}. They involve roles such as {keywords}."
            response = await embeddings_model.get_response(context=context, session=session)
            return {
                "Category": category,
                "Definition": definition,
                "Keywords": keywords,
                "Input": context,
                "Embedding": response["output"]
            }

        """
        Load or renew categories embeddings.

        :param renew: Whether to renew the categories embeddings.
        """
        categories_path = Ledger().tree.get_path(desc="file_categories_index")
        self.categories = self.files.read_df(categories_path, dtype="pkl")
        if self.categories is None or self._renew_categories:
            embeddings_model = OpenAI(self.ledger["models"]["embeddings"])
            async with aiohttp.ClientSession() as session:
                tasks = [get_embedding(c, d, k) for c, d, k in category_keymap]
                categories = await asyncio.gather(*tasks)
            self.categories = pd.DataFrame(categories)
            self.files.write_df(categories_path, self.categories, dtype="pkl")

    def fetch_jobs_list(self, platform: str = "glassdoor", renew: bool = False) -> dict:
        """
        Fetch jobs list from the specified platform.
        :param platform: The platform to fetch jobs from.
        :param renew:  Whether to renew the job descriptions.
        :return:  The fetched jobs list.
        """
        if renew:
            if platform == "glassdoor":
                Glassdoor(
                    keywords=self.preferences["roles"],
                    locations=self.preferences["locations"],
                    credentials=self.preferences["credentials"]["glassdoor"],
                    out_path=self.paths["files"]["descriptions"],
                    incl_path=self.paths["files"]["jobs_hash_idx"]
                ).fetch()
            else:
                raise ValueError("Platform not supported yet.")
        jobs_list = self.files.read_json(self.paths["files"]["descriptions"], default={})
        if jobs_list == {}:
            return self.fetch_jobs_list(platform=platform, renew=True)
        return jobs_list


if __name__ == "__main__":
    data = Data("AmirMasoud Azadfar", "glassdoor")
    asyncio.run(data.prepare_data())
