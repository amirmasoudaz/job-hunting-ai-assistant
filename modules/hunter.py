import asyncio
from datetime import datetime
import os

import aiohttp

from modules.data import Data
from modules.analysis import Analyzer
from configs import apps_template, logs_template


class Hunter:
    def __init__(
            self,
            user_name: str,
            platform: str = "glassdoor",
            renew_descriptions: bool = False,
            batch_process: bool = False,
            customize_apps: bool = False,
    ):
        self._batch_process = batch_process
        self._customize = customize_apps
        self._date = datetime.now().strftime("%m-%d-%Y")

        self.data = Data(user_name, platform, renew_descriptions=renew_descriptions)
        self.analyzer = Analyzer()

        self.apps = {}
        self.logs = {}

    async def sequential_process(self, app, log):
        """
        Process a job application.
        :param app: Application dictionary.
        :param log: Log dictionary.
        :return: Tuple of updated application and log.
        """
        app, log = await self.analyzer.get_moderation(app, log, self.data.preferences)
        if not app["moderation"]:
            return app, log

        app, log = await self.analyzer.get_description(app, log)
        app, log = await self.analyzer.get_category(app, log, self.data.categories, self.data.preferences)
        if not app["category_pass"]:
            return app, log

        app, log = await self.analyzer.get_role_comp(app, log, self.data.resume_md, self.data.preferences)
        if not app["role_cpass"]:
            return app, log

        app, log = await self.analyzer.get_app_comp(app, log, self.data.resume_md)
        if not app["app_cpass"] and not app["match_cpass"]:
            return app, log

        if self._customize:
            if input("Generate Cover Letter? (y/n): ").lower() == "y":
                app, log = await self.analyzer.customize_letter(app, log, resume_md=self.data.resume_md)
            if input("Generate Email? (y/n): ").lower() == "y":
                app, log = await self.analyzer.get_email(app, log, resume_md=self.data.resume_md)
        return await self.analyzer.gen_report(app, log)

    async def sequential_process_all(self):
        for uid in self.apps:
            app, log = await self.sequential_process(
                app=self.apps[uid],
                log=self.logs[uid])
            app, log = await self.analyzer.save_application(app, log)
            print(app["report"] + f"Cost: {app["usage"]["total_cost"]:.8f}")
            self.apps[uid], self.logs[uid] = app, log

    async def batch_process_all(self):
        await self.batch_get_moderation()
        await self.batch_get_description()
        await self.batch_get_category()
        await self.batch_get_role_comp()
        await self.batch_get_app_comp()
        results = await self.batch_gen_report()
        await self.apply_to_jobs(results)

    @staticmethod
    def get_batch_stats(results, key, title):
        passed = sum([1 for app, _ in results if app[key]])
        print(f"{title} results | Fail: {len(results) - passed}, Pass: {passed}")

    async def finalize_batch_results(self, results):
        to_save_tasks = []
        for app, log in results:
            to_save_tasks.append(self.analyzer.save_application(app, log))
            self.apps[app["uid"]], self.logs[app["uid"]] = app, log
        await asyncio.gather(*to_save_tasks)

    async def batch_get_moderation(self):
        cost, count = 0, 0
        for uid, app in self.apps.items():
            self.apps[uid], context = self.analyzer.get_moderation_context(self.apps[uid], self.data.preferences)
            cost += self.apps[uid]["costs"]["moderation"]
            count += 1
        print(f"Moderation | Cost: {cost:.4f} | Count: {count}", end=" | ")
        results = await asyncio.gather(*[
            self.analyzer.get_moderation(app, self.logs[uid], self.data.preferences)
            for uid, app in self.apps.items()
        ])
        await self.finalize_batch_results(results)
        self.get_batch_stats(results, "moderation", "Moderation")

    async def batch_get_description(self):
        cost, count = 0, 0
        for uid, app in self.apps.items():
            if not app["moderation"]:
                continue
            self.apps[uid], _ = self.analyzer.get_description_context(app)
            cost += self.apps[uid]["costs"]["description"]
            count += 1
        print(f"Description | Cost: {cost:.4f} | Count: {count}")
        results = await asyncio.gather(*[
            self.analyzer.get_description(app, self.logs[uid])
            for uid, app in self.apps.items() if app["moderation"]
        ])
        await self.finalize_batch_results(results)

    async def batch_get_category(self):
        cost, count = 0, 0
        for uid, app in self.apps.items():
            if not app.get("moderation", False):
                continue
            self.apps[uid], _ = self.analyzer.get_category_context(app)
            cost += self.apps[uid]["costs"]["category"]
            count += 1
        print(f"Category | Cost: {cost:.4f} | Count: {count}", end=" | ")
        results = await asyncio.gather(*[
            self.analyzer.get_category(app, self.logs[uid], self.data.categories, self.data.preferences)
            for uid, app in self.apps.items() if app["moderation"]
        ])
        await self.finalize_batch_results(results)
        self.get_batch_stats(results, "category_pass", "Category")

    async def batch_get_role_comp(self):
        cost, count = 0, 0
        for uid, app in self.apps.items():
            if not app.get("category_pass", False):
                continue
            self.apps[uid], _, _ = self.analyzer.get_role_comp_context(app, self.data.resume_md, self.data.preferences)
            cost += self.apps[uid]["costs"]["role_comp"]
            count += 1
        print(f"Role Comp | Cost: {cost:.4f} | Count: {count}", end=" | ")
        results = await asyncio.gather(*[
            self.analyzer.get_role_comp(app, self.logs[uid], self.data.resume_md, self.data.preferences)
            for uid, app in self.apps.items() if app.get("category_pass", False)
        ])
        await self.finalize_batch_results(results)
        self.get_batch_stats(results, "role_cpass", "Role Comp")

    async def batch_get_app_comp(self):
        cost, count = 0, 0
        for uid, app in self.apps.items():
            if not app.get("role_cpass", False):
                continue
            self.apps[uid], _, _ = self.analyzer.get_app_comp_context(app, self.data.resume_md)
            cost += self.apps[uid]["costs"]["app_comp"]
            count += 1
        print(f"App Comp | Cost: {cost:.4f} | Count: {count}", end=" | ")
        results = await asyncio.gather(*[
            self.analyzer.get_app_comp(app, self.logs[uid], self.data.resume_md)
            for uid, app in self.apps.items() if app.get("role_cpass", False)
        ])
        await self.finalize_batch_results(results)
        self.get_batch_stats(results, "app_cpass", "App Comp")
        self.get_batch_stats(results, "match_cpass", "Match Comp")

    async def batch_gen_report(self):
        results = await asyncio.gather(*[
            self.analyzer.gen_report(app, self.logs[uid])
            for uid, app in self.apps.items() if app.get("app_cpass", False) or app.get("match_cpass", False)
        ])
        await self.finalize_batch_results(results)
        return results

    async def apply_to_jobs(self, results):
        job_count = 0
        print("\n\nFinal Results:")
        for app, log in results:
            # add any other conditions here
            if "remote" in app["description"]["Location"].lower():
                print(f"{job_count + 1}", end=". ")
                print(f"{app["description"]["Location"]} {app["report"]}\n\n{app["final_report"]}")
                if input("Generate Cover Letter? (y/n): ").lower() == "y":
                    if not app["paths"].get("letter_path"):
                        app["paths"]["letter_path"] = app["paths"]["app_path"].replace("cache.json", "")
                    app, log = await self.analyzer.customize_letter(app, log, resume_md=self.data.resume_md)
                if input("Generate Email? (y/n): ").lower() == "y":
                    if not app["paths"].get("email_path"):
                        app["paths"]["email_path"] = app["paths"]["app_path"].replace("cache.json", "email.txt")
                    app, log = await self.analyzer.get_email(app, log, resume_md=self.data.resume_md)
                await self.analyzer.save_application(app, log)
                job_count += 1

    def get_app(self, app: dict) -> tuple:
        """
        Retrieve or create an application and its log.

        :param app: Application dictionary.
        :return: Tuple containing the updated application and its log.
        """
        uid: str = self.data.files.normalize_path(f"{app['company']} - {app['title']} - {app["hash"]}")
        app_dir = os.path.join(self.data.paths["dirs"]["applications"], uid)
        app_path = os.path.join(app_dir, "cache.json")
        log_path = os.path.join(app_dir, "log.json")
        ready_path = os.path.join(app_dir, "ready.json")

        os.makedirs(app_dir, exist_ok=True)

        if os.path.exists(ready_path):
            cache = self.data.files.read_json(ready_path)
            log = self.data.files.read_json(log_path)
        elif os.path.exists(app_path):
            cache = self.data.files.read_json(app_path)
            log = self.data.files.read_json(log_path)
        else:
            cache = {
                **apps_template.copy(),
                "now": self._date,
                "uid": uid,
                "paths": {
                    "app_dir": app_dir,
                    "app_path": app_path,
                    "log_path": log_path,
                    "ready_path": ready_path,
                    "report_path": os.path.join(app_dir, "report.txt"),
                    "letter_docx_path": os.path.join(app_dir, "letter.docx"),
                    "letter_pdf_path": os.path.join(app_dir, "letter.pdf"),
                    "email_path": os.path.join(app_dir, "email.txt"),
                }
            }
            log = logs_template.copy()
        app.update(cache)
        self.data.files.write_json(app_path, app, indent=4)
        self.data.files.write_json(log_path, log, indent=4)

        return app, log

    def gen_apps(self):
        """
        Generate job applications automatically from descriptions.
        """
        for job_hash, job_data in self.data.jobs_list.items():
            app = {
                "company": job_data["company"],
                "title": job_data["title"],
                "location": f"{job_data["location"]} - {job_data["search_location"]}",
                "posted_date": job_data["posted"] + " ago",
                "raw_description": job_data["details"],
                "more_details": {
                    key: job_data[key] for key in [
                        "rating", "salary", "overview",
                        "reviews", "ratings", "scores"
                    ] if job_data[key] not in ["N/A", "--", {}]
                },
                "metadata": {
                    key: job_data[key] for key in [
                        "url", "url_hash", "search_keyword",
                        "search_location", "created_at"
                    ]
                },
                "hash": job_hash
            }
            app, log = self.get_app(app)
            self.apps[app["uid"]] = app
            self.logs[app["uid"]] = log

    async def process_apps(self):
        self.gen_apps()
        async with aiohttp.ClientSession() as self.analyzer.session:
            if self._batch_process:
                await self.batch_process_all()
            else:
                await self.sequential_process_all()
