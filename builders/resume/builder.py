import base64
import os
from pathlib import Path

from selenium.webdriver.common.by import By

from tools import Files, Chrome
from builders.resume import blocks


class ResumeBuilder:
    _headless: bool = False
    _theme: str = "light"

    def __init__(self):
        self._files = Files()

        root = os.path.dirname(os.path.dirname(__file__))
        self.templates_path = os.path.join(root, "resume", "templates")
        self.temporary_path = os.path.join(root, "resume", "temporary")
        if os.path.exists(self.temporary_path):
            self._files.delete_dir(self.temporary_path)
        self._files.copy_dir(self.templates_path, self.temporary_path)

        self.html_path = os.path.join(self.temporary_path, "index.html")

    def build(
            self,
            data: dict,
            path: str,
            file_name: str,
            del_tmp_files: bool = True,
            include_summary: bool = False,
            hyperlink_decorations: bool = False
    ):
        data.update(data.pop("info", {}))

        html = self._files.read_file(self.html_path)
        html = html.format(
            user_name=data["name"],
            styles=self.get_styles(hyperlink_decorations),
            summary_block=self.get_summary(data, include_summary),
            header_block=self.get_header(data),
            skills_block=self.get_skills(data),
            works_block=self.get_works(data),
            projects_block=self.get_projects(data),
            education_block=self.get_education(data),
            certificates_block=self.get_certificates(data))
        self._files.write_file(self.html_path, html, encoding="utf-8")

        chrome = self.start_driver()
        chrome.driver.get(Path(self.html_path).resolve().as_uri())
        chrome.driver.set_window_size(2000, 2000)
        container_size = chrome.driver.find_element(By.CLASS_NAME, "container").size
        height = container_size['height'] + 2 * 48
        width = container_size['width'] + 2 * 48
        chrome.driver.set_window_size(width, height)
        divider = 96
        pdf_options = {
            "landscape": False,
            "displayHeaderFooter": False,
            "printBackground": True,
            "preferCSSPageSize": False,
            "paperWidth": width / divider,
            "paperHeight": height / divider,
            "marginTop": 0.05,
            "marginBottom": 0.05,
            "marginLeft": 0.05,
            "marginRight": 0.05
        }
        result_base64 = chrome.driver.execute_cdp_cmd("Page.printToPDF", pdf_options)
        result = base64.b64decode(result_base64['data'])
        path = os.path.join(path, f"{file_name}.pdf")
        self._files.write_file(path, result, mode="wb")
        self._files.delete_dir(self.temporary_path) if del_tmp_files else None

        del chrome

    @staticmethod
    def add_kwargs(**kwargs):
        kwargs = ' '.join([f'{key}="{value}"' for key, value in kwargs.items()])
        return " " + kwargs if kwargs else ""

    def a(self, text: str = "", hidden_text: str = "", **kwargs):
        return f'<a{self.add_kwargs(**kwargs)}>{text}<span class="hidden">{hidden_text}</span></a>'

    def li(self, text: str, hidden_text: str = "", **kwargs):
        return f'<li{self.add_kwargs(**kwargs)}>{text}<span class="hidden">{hidden_text}</span></li>'

    def start_driver(self):
        options_args = [
            "--disable-extensions"
            "--disable-gpu"
        ]
        if self._headless:
            options_args.append("--headless")
        experimental_args = [
            ['prefs', {'intl.accept_languages': 'en,en_US'}]
        ]
        chrome = Chrome(
            mode="default",
            options_args=options_args,
            experimental_args=experimental_args
        )
        chrome.driver.execute_cdp_cmd('Emulation.setEmulatedMedia', {
            'features': [{'name': 'prefers-color-scheme', 'value': self._theme}]
        })

        return chrome

    @staticmethod
    def get_styles(hyperlink_decorations: bool = True):
        styles = []
        if hyperlink_decorations:
            styles.append(blocks.hyperlink_transparency_style)
        return "\n".join(styles)

    @staticmethod
    def get_duration(duration):
        if isinstance(duration, str):
            return duration
        elif isinstance(duration, dict):
            if duration.get("from") and duration.get("till"):
                if duration["from"] == duration["till"]:
                    return duration["from"]
                return f"{duration['from']} - {duration['till']}"
        return ""

    def get_hyperlink(self, item):
        if not item.get("url") or not item["url"].get("title"):
            return ""
        else:
            return f" | {self.a(item["url"]["title"], href=item["url"]["link"])}"

    def get_header(self, data):
        location = ', '.join(data[field] for field in ['city', 'state/province', 'country'] if data.get(field))
        contact = ' | '.join(data[field] for field in ['email', 'phone'] if data.get(field))
        if data.get("social_media", None):
            socials = ' | '.join(
                self.a(text=social["platform"], href=social["url"])
                for social in data["social_media"])
            contact = f"{contact} | {socials}" if contact else socials
        content = f"{location} | {contact}" if contact else location
        header_block = blocks.header_block.format(
            name=data.get("name", "NO NAME"),
            expertise=data.get("title", "NO EXPERTISE"),
            content=content)
        return header_block

    @staticmethod
    def get_summary(data, include_summary: bool = True):
        if include_summary:
            return blocks.summary_block.format(summary=data["summary"])
        return ""

    def get_skills(self, data):
        if not data.get("skills"):
            return ""

        skill_groups = []
        for i, skills in enumerate(data["skills"]):
            skills_list = "".join(self.li(skill) for skill in skills["skills"])
            affix = "even" if i % 2 == 0 else "odd"
            group_block = blocks.skill_group_block.format(
                title=skills["title"],
                affix=affix,
                skills=skills_list)
            skill_groups.append(group_block)
        html_block = blocks.skills_heading + "\n" + "\n".join(skill_groups)
        return html_block

    def get_works(self, data):
        if not data.get("work"):
            return ""

        jobs_list = []
        for i, item in enumerate(data["work"]):
            tasks = []
            if isinstance(item["details"], dict):
                for title, task in item["details"].items():
                    tasks.append(f"<strong>{title}</strong>: {task}")
            elif isinstance(item["details"], list):
                tasks = item["details"]
            tasks = "".join(self.li(task) for task in tasks)
            margin_bottom = "2" if i == len(data["work"]) - 1 else "3"
            work_block = blocks.work_experience_block.format(
                role=item["position"],
                company=item["company"],
                hyperlink=self.get_hyperlink(item),
                duration=self.get_duration(item["duration"]),
                margin_bottom=margin_bottom,
                tasks=tasks)
            jobs_list.append(work_block)
        return blocks.work_experience_headings + "\n" + "\n".join(jobs_list)

    def get_projects(self, data):
        if not data.get("project"):
            return ""

        projects_list = []
        for i, item in enumerate(data["project"]):
            tasks = "".join(self.li(task) for task in item["details"])
            margin_bottom = "2" if i == len(data["project"]) - 1 else "3"
            project_block = blocks.project_block.format(
                title=item["name"],
                duration=self.get_duration(item["duration"]),
                hyperlink=self.get_hyperlink(item),
                margin_bottom=margin_bottom,
                tasks=tasks)
            projects_list.append(project_block)
        return blocks.projects_heading + "\n" + "\n".join(projects_list)

    def get_education(self, data):
        if not data.get("education"):
            return ""

        educations_list = []
        for education in data["education"]:
            education_block = blocks.education_block.format(
                title=education["degree"],
                institution=education["institution"],
                duration=self.get_duration(education["duration"]))
            educations_list.append(education_block)
        return blocks.education_heading + "\n" + "\n".join(educations_list)

    def get_certificates(self, data):
        if not data.get("certifications"):
            return ""

        certifications_list = []
        for item in data["certifications"]:
            certification_block = blocks.certificate_block.format(
                title=item["title"],
                institution=item["institution"],
                hyperlink=self.get_hyperlink(item),
                date=self.get_duration(item["date"]))
            certifications_list.append(certification_block)
        return blocks.certificates_heading + "\n" + "\n".join(certifications_list)


if __name__ == "__main__":
    from builders.resume.samples import sample as sample

    root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(root, "resume", "outputs")
    ResumeBuilder().build(
        data=sample, path=path,
        file_name="Sample",
        include_summary=True,
        del_tmp_files=False)
