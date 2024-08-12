import json

import pandas as pd
from scipy.spatial.distance import cosine

from agents import Agents
from gpt import OpenAI
from tools import Files, JSONFormatting, Ledger
from builders import LetterBuilder


class Analyzer:
    def __init__(self):
        self._ledger = Ledger().analyzer
        self._agents = Agents()
        self._files = Files()
        self._formatting = JSONFormatting()

        self._gpt_embeddings = OpenAI(self._ledger["models"]["embeddings"])
        self._gpt_efficient = OpenAI(self._ledger["models"]["efficient"])
        self._gpt_proficient = OpenAI(self._ledger["models"]["proficient"])

        self.session = None

    @staticmethod
    def calc_total_usage(log: dict) -> dict:
        """
        Calculate total resource usage for the application.
        :param log: Log dictionary.
        :return: Dictionary of total usage.
        """
        usage = {"input_tokens": 0, "input_cost": 0, "output_tokens": 0, "output_cost": 0}
        for info in log.values():
            if not info:
                continue
            usage["input_tokens"] += info["usage"]["input_tokens"]
            usage["input_cost"] += info["usage"]["input_cost"]
            if "output_tokens" not in info["usage"]:
                continue
            usage["output_tokens"] += info["usage"]["output_tokens"]
            usage["output_cost"] += info["usage"]["output_cost"]
        usage["total_tokens"] = usage["input_tokens"] + usage["output_tokens"]
        usage["total_cost"] = usage["input_cost"] + usage["output_cost"]
        return usage

    async def save_application(self, app: dict, log: dict, ready: bool = False) -> tuple:
        """
        Save the application data and log to files.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param ready: Whether the application is ready for final save.
        :return: Tuple of updated application and log.
        """
        app["usage"] = self.calc_total_usage(log)
        await self._files.write_json_async(app["paths"]["app_path"], app, indent=4)
        await self._files.write_json_async(app["paths"]["log_path"], log, indent=4)
        if ready:
            self._files.write_json(app["paths"]["ready_path"], app, indent=4)
            self._files.write_file(app["paths"]["report_path"], app["final_report"])

        return app, log

    @staticmethod
    def add_report(app: dict, content: str, open_ended: bool = True):
        """
        Add content to the application report.

        :param app: Application dictionary.
        :param content: Report content.
        :param open_ended: Whether the content is open-ended.
        """
        if "report" not in app:
            app["report"] = ""
        app["report"] += content
        if open_ended:
            app["report"] += " "
        else:
            app["report"] += "\n"
        return app

    async def gen_report(self, app: dict, log: dict) -> tuple:
        """
        Generate a final report for the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :return: Tuple of updated application and log.
        """
        description = app["description"].copy()
        app["final_report"] = "- " + " | ".join([
            description.pop(key, "N/A")
            for key in ["Location", "Employment Type", "Industry", "Field of Work"]
        ])
        app["final_report"] += "\n\n" + "\n".join([
            f"- {key.capitalize()} -> {value}"
            for key, value in description.items()
            if key not in ["Position Name", "Company Name"]
        ])

        if not self._ledger["modes"]["eco_mode"]:
            for key in ["threats", "weaknesses", "strengths", "opportunities"]:
                if app.get(key, None):
                    app["final_report"] += f"\n\n- {key.capitalize()}:\n"
                    app["final_report"] += "\n".join([f"- {item[0]} -> {item[1]}" for item in app[key].values()])

        return await self.save_application(app, log, ready=True)

    def get_letter_context(self, app: dict, resume_md: dict) -> tuple:
        context = [{"content": self._agents.letter_customization, "role": "system"}]
        for content in [
            f"ROLE DESCRIPTION: ~~~{json.dumps(app["description"], indent=4)}~~~",
            f"RESUME: ###{json.dumps(resume_md, indent=4)}###"
        ]:
            context.append({"content": content, "role": "user"})
        cost = self.eval_cost(
            tokenizer=self._gpt_proficient.client.tokenizer,
            context=context, output=0.1)
        app["costs"]["letter"] = cost
        return app, context

    async def customize_letter(self, app: dict, log: dict, resume_md: dict) -> tuple:
        """
        Generate a cover letter for the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param resume_md: Resume markdown dictionary.
        :return: Tuple of updated application and log.
        """
        if app["letter"] is not None and app["letter"].get("final"):
            return app, log
        if log["letter"] is None:
            app, log["letter"] = self.get_letter_context(app, resume_md)
        while True:
            response = await self._gpt_proficient.get_response(
                context=log["letter"], response_format="json_object",
                identifier=f"{app["uid"]}_letter", session=self.session)
            print(response["output"])
            if input("Is the letter okay now? (Y/N): ").lower() == "y":
                break
            else:
                log["letter"].append({"content": response["output"], "role": "assistant"})
                user_feedback = input("What would you like to change? ")
                if input("Would you like to add more context? (Y/N): ").lower() == "y":
                    more_context = input("Please provide more context: ")
                    user_feedback += f"\n\n{more_context}"
                print("Submitting feedback...")
                log["letter"].append({"content": user_feedback, "role": "user"})
        print("Populating the letter document template with the final response...")
        builder = LetterBuilder(template="simple")
        builder.build(data=response["output"], path=app["paths"]["letter_path"], file_name="letter")
        app["letter"] = {
            "result": response["output"],
            "final": True
        }
        return app, log

    def get_email_context(self, app: dict, resume_md: dict) -> tuple:
        context = [{"content": self._agents.email_customization, "role": "system"}]
        for content in [
            f"ROLE DESCRIPTION: ~~~{json.dumps(app["description"], indent=4)}~~~",
            f"RESUME: ###{json.dumps(resume_md, indent=4)}###"
        ]:
            context.append({"content": content, "role": "user"})
        cost = self.eval_cost(
            tokenizer=self._gpt_proficient.client.tokenizer,
            context=context, output=0.1)
        app["costs"]["email"] = cost
        return app, context

    async def get_email(self, app: dict, log: dict, resume_md: dict) -> tuple:
        """
        Generate email for the application.
        """
        if app["email"] is not None and app["letter"].get("final"):
            return app, log
        if log["email"] is None:
            app, log["email"] = self.get_letter_context(app, resume_md)
        while True:
            response = await self._gpt_proficient.get_response(
                context=log["email"], response_format="json_object",
                identifier=f"{app["uid"]}_email", session=self.session)
            print(response["output"])
            if input("Is the email okay now? (Y/N): ").lower() == "y":
                break
            else:
                log["letter"].append({"content": response["output"], "role": "assistant"})
                user_feedback = input("What would you like to change? ")
                if input("Would you like to add more context? (Y/N): ").lower() == "y":
                    more_context = input("Please provide more context: ")
                    user_feedback += f"\n\n{more_context}"
                print("Submitting feedback...")
                log["letter"].append({"content": user_feedback, "role": "user"})
        app["email"] = {
            "result": response["output"],
            "final": True
        }
        return app, log

    def get_comp_score(self, analysis, weights, ctype="app"):
        """
        Calculate compatibility score.

        :param analysis: Analysis result.
        :param weights: Weight set.
        :param ctype: Compatibility type.
        :return: Compatibility score and impacts.
        """
        cscore, impacts = 0, {"Yes": {}, "No": {}}
        if self._ledger["modes"]["eco_mode"]:
            for key, value in analysis.items():
                impact = 1 if value == "Yes" else 0
                title, score = weights.get(int(key), ["Unknown", 0])
                impacts[value][key] = [title, score]
                cscore += score * impact
        else:
            for key, value in analysis.items():
                impact = 1 if value[0] == "Yes" else 0
                title, score = weights.get(int(key), ["Unknown", 0])
                impacts[value[0]][key] = [title, value[1]]
                cscore += score * impact

        if "app" in ctype:
            return {"app_cscore": cscore, "strengths": impacts["Yes"], "weaknesses": impacts["No"]}
        elif "role" in ctype:
            return {"role_cscore": cscore, "opportunities": impacts["Yes"], "threats": impacts["No"]}
        else:
            return {"cscore": cscore, "pluses": impacts["Yes"], "minuses": impacts["No"]}

    def get_q_str_n_w_set(self, q_set):
        """
        Convert question set to string and weight set.

        :param q_set: Question set.
        :return: Tuple of question string and weight set.
        """
        q_str = self._formatting.stringify(obj={attr[0]: attr[2] for attr in q_set}, kv_connector=".")
        w_set = {attr[0]: [attr[1], attr[3]] for attr in q_set}
        return q_str, w_set

    def get_role_comp_context(self, app: dict, resume_md: dict, preferences: dict) -> tuple:
        q_str, w_set = self.get_q_str_n_w_set(self._agents.description_questions)
        if not self._ledger["modes"]["eco_mode"]:
            prompt = self._agents.description_compatibility
            template = {i: [] for i in range(1, len(w_set) + 1)}
        else:
            prompt = self._agents.description_compatibility_eco
            template = {i: "" for i in range(1, len(w_set) + 1)}

        context = prompt.format(
            user_resume="\n".join(resume_md.values()),
            desired_job_titles=preferences["roles"],
            desired_involved_skills=preferences["skills"],
            template=json.dumps(template, indent=4),
            questions=q_str)
        content = json.dumps(app["description"], indent=4)
        context = [
            {"content": context, "role": "system"},
            {"content": content, "role": "user"}
        ]
        cost = self.eval_cost(
            tokenizer=self._gpt_proficient.client.tokenizer,
            context=context, output=0.1)
        app["costs"]["role_comp"] = cost
        return app, context, w_set

    async def get_role_comp(self, app: dict, log: dict, resume_md: dict, preferences: dict) -> tuple:
        """
        Get the job description's compatibility score for the application based on the user's resume.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param resume_md: Resume markdown dictionary.
        :param preferences: User preferences dictionary.
        :return: Tuple of updated application and log.
        """
        if app["role_cscore"] is not None and not self._ledger["modes"]["reprocessing"]:
            return app, log
        if not self._ledger["models"]["role_compatibility"]:
            app["role_cpass"] = True
            return app, log

        app, context, w_set = self.get_role_comp_context(app, resume_md, preferences)
        while True:
            log["role_comp"] = await self._gpt_proficient.get_response(
                context=context, response_format="json_object",
                identifier=f"{app["uid"]}_role_comp", session=self.session)
            if not self._ledger["modes"]["eco_mode"]:
                yes_nos = [value[0] for value in log["role_comp"]["output"].values()]
                if all([yn in ["Yes", "No"] for yn in yes_nos]):
                    break
            else:
                yes_nos = list(log["role_comp"]["output"].values())
                if all([yn in ["Yes", "No"] for yn in yes_nos]):
                    break
        app.update(self.get_comp_score(log["role_comp"]["output"], w_set, ctype="role"))
        app, log = self.check_alignment(app, log, ctype="role")
        if not app["role_cpass"]:
            app = self.add_report(app, content=f"- NOT OK -", open_ended=True)  # False if printing into console
        return app, log

    def get_app_comp_context(self, app: dict, resume_md: dict) -> tuple:
        q_str, w_set = self.get_q_str_n_w_set(self._agents.application_questions[app["category"]])
        if not self._ledger["modes"]["eco_mode"]:
            prompt = self._agents.application_compatibility
            template = {i: [] for i in range(1, len(w_set) + 1)}
        else:
            prompt = self._agents.application_compatibility_eco
            template = {i: "" for i in range(1, len(w_set) + 1)}
        context = prompt.format(
            user_resume="\n".join(resume_md.values()),
            template=json.dumps(template, indent=4),
            questions=q_str)
        content = json.dumps(app["description"], indent=4)
        context = [
            {"content": context, "role": "system"},
            {"content": content, "role": "user"}
        ]
        cost = self.eval_cost(
            tokenizer=self._gpt_proficient.client.tokenizer,
            context=context, output=0.3)
        app["costs"]["app_comp"] = cost
        return app, context, w_set

    async def get_app_comp(self, app: dict, log: dict, resume_md: dict) -> tuple:
        """
        Get the applicant's resume's compatibility score for the application based on the job description.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param resume_md: Resume markdown dictionary.
        :return: Tuple of updated application and log.
        """
        if app["app_cscore"] is not None and not self._ledger["modes"]["reprocessing"]:
            return app, log

        app, context, w_set = self.get_app_comp_context(app, resume_md)
        while True:
            log["app_comp"] = await self._gpt_proficient.get_response(
                context=context, response_format="json_object",
                identifier=f"{app["uid"]}_app_comp", session=self.session)
            if not self._ledger["modes"]["eco_mode"]:
                yes_nos = [value[0] for value in log["app_comp"]["output"].values()]
                if all([yn in ["Yes", "No"] for yn in yes_nos]):
                    break
            else:
                yes_nos = list(log["app_comp"]["output"].values())
                if all([yn in ["Yes", "No"] for yn in yes_nos]):
                    break
        app.update(self.get_comp_score(log["app_comp"]["output"], w_set, ctype="app"))
        app, log = self.check_alignment(app, log, ctype="app")
        app, log = self.check_alignment(app, log, ctype="match")
        if not app["app_cpass"] and not app["match_cpass"]:
            app = self.add_report(app, content=f"- NOT OK -", open_ended=True)  # False if printing into console
        else:
            app = self.add_report(app, content=f"- OK -", open_ended=True)  # False if printing into console
        return app, log

    def check_alignment(self, app: dict, log: dict, ctype="match"):
        def grade_converter(grade: int):
            """
            Convert numerical grade to letter grade
            :param grade: Numerical grade
            :return:
            """
            grade_keymap = {
                97: "A+", 93: "A", 90: "A-",
                87: "B+", 83: "B", 80: "B-",
                77: "C+", 73: "C", 70: "C-",
                67: "D+", 63: "D", 60: "D-",
                59: "F"
            }
            for key in sorted(grade_keymap.keys(), reverse=True):
                if grade >= key:
                    return grade_keymap[key]
            return "F"

        """
        Check alignment of the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param ctype: Compatibility type.
        """
        app = self.add_report(app, content=f"| {ctype.upper()}")
        if ctype == "match":
            role_comp, app_comp = app["role_cscore"], app["app_cscore"]
            role_cs = role_comp * self._ledger["match_weights"]["role"]
            app_cs = app_comp * self._ledger["match_weights"]["app"]
            app["match_cscore"] = round(role_cs + app_cs, 2)

        app.update({
            f"{ctype}_cpass": app[f"{ctype}_cscore"] >= self._ledger["cs_thr"][ctype],
            f"{ctype}_cgrade": grade_converter(app[f"{ctype}_cscore"])
        })
        app = self.add_report(app, content=f"{app[f'{ctype}_cscore']}% ({app[f'{ctype}_cgrade']})")
        return app, log

    def get_category_context(self, app: dict) -> tuple:
        context = self._formatting.stringify(app["description"])
        cost = self.eval_cost(
            tokenizer=self._gpt_embeddings.client.tokenizer,
            context=context, embeddings=True)
        app["costs"]["category"] = cost
        return app, context

    async def get_category(self, app: dict, log: dict, categories: pd.DataFrame, preferences: dict) -> tuple:
        """
        Get job category for the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param categories: Categories dataframe.
        :param preferences: User preferences dictionary.
        :return: Tuple of updated application and log.
        """
        if app["category"] is not None and not self._ledger["modes"]["reprocessing"]:
            return app, log
        if not self._ledger["modes"]["categorization"]:
            app["category_pass"] = True
            app["category"] = preferences["category"]
            return app, log

        app, context = self.get_category_context(app)
        log["category"] = await self._gpt_embeddings.get_response(
            context=context, identifier=f"{app["uid"]}_category",
            session=self.session)

        vector = log["category"]["output"]
        table = [
            (row["Category"], 1 - cosine(row["Embedding"], vector))
            for i, row in categories.iterrows()
        ]
        category, log["category"]["similarity"] = sorted(table, key=lambda x: x[1], reverse=True)[0]
        app["category_pass"] = category == preferences["category"] or not self._ledger["modes"]["categorization"]
        app["category"] = category

        app = self.add_report(app, content=f"| CAT {app["category"]}")
        if not app["category_pass"]:
            app = self.add_report(app, content=f"- NOT OK -", open_ended=True)  # False if printing into console
        return app, log

    def get_description_context(self, app: dict) -> tuple:
        context = self._agents.description_normalization
        content = json.dumps({
            " ".join([k.capitalize() for k in key.split("_")]): value
            for key, value in app.items()
            if key in ["company", "title", "location", "raw_description"]
        }, indent=4)
        context = [
            {"content": context, "role": "system"},
            {"content": content, "role": "user"}
        ]
        cost = self.eval_cost(
            tokenizer=self._gpt_efficient.client.tokenizer,
            context=context, output=0.1)
        app["costs"]["description"] = cost
        return app, context

    async def get_description(self, app: dict, log: dict) -> tuple:
        """
        Get job description for the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :return: Tuple of updated application and log.
        """
        if app["description"] is not None and not self._ledger["modes"]["reprocessing"]:
            return app, log

        app, context = self.get_description_context(app)
        log["description"] = await self._gpt_efficient.get_response(
            context=context, response_format="json_object",
            identifier=f"{app["uid"]}_description", session=self.session)
        app["description"] = log["description"]["output"]
        app = self.add_report(app, content=f"| DES")
        return app, log

    def get_moderation_context(self, app: dict, preferences: dict) -> tuple:
        """
        Get moderation context for the application.
        :param app: Application dictionary.
        :param preferences: User preferences dictionary.
        :return: List of context strings.
        """
        context = self._agents.description_preprocessing.format(
            role_preferences=preferences["roles"],
            skills_preferences=preferences["skills"],
            stack_preferences=preferences["stack"])
        content = f"```JOB:\nTITLE: {app["title"]}\nCOMPANY: {app["company"]}\nDESCRIPTION: {app["raw_description"]}```"
        context = [
            {"content": context, "role": "system"},
            {"content": content, "role": "user"}
        ]
        cost = self.eval_cost(
            tokenizer=self._gpt_efficient.client.tokenizer,
            context=context, output=1)
        app["costs"]["moderation"] = cost
        return app, context

    async def get_moderation(self, app: dict, log: dict, preferences: dict) -> tuple:
        """
        Get moderation status for the application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :param preferences: User preferences dictionary.
        :return: Tuple of updated application and log.
        """
        if app["moderation"] is not None and not self._ledger["modes"]["reprocessing"]:
            return app, log

        app = self.add_report(app, content=f"- {app["title"]} at {app["company"]} | INIT")
        app, context = self.get_moderation_context(app, preferences)
        log["moderation"] = await self._gpt_efficient.get_response(
            context=context, max_tokens=1, response_format="text",
            identifier=f"{app["uid"]}_moderation", session=self.session)
        app["moderation"] = log["moderation"]["output"] == "Y"
        app = self.add_report(app, content=f"| MOD")
        if not app["moderation"]:
            app = self.add_report(app, content=f"- NOT OK -", open_ended=True)  # False if printing into console
        return app, log

    @staticmethod
    def eval_cost(tokenizer, context, output: float = 1.0, embeddings: bool = False) -> float:
        if isinstance(context, int) and embeddings:
            prompt_tokens = context
        else:
            prompt_tokens = tokenizer.count_tokens(context)
        if embeddings:
            return tokenizer.parse_usage({
                "prompt_tokens": prompt_tokens,
                "total_tokens": prompt_tokens
            })["input_cost"]
        if 0 < output < 1:
            output = round(output * prompt_tokens)
        return tokenizer.parse_usage({
            "prompt_tokens": prompt_tokens,
            "completion_tokens": output,
            "total_tokens": prompt_tokens + output
        })["total_cost"]
