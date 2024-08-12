from datetime import datetime, UTC
import hashlib
import os
import random
import re
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4.element import Tag

from tools import Files, Chrome, Ledger


class Glassdoor:
    def __init__(self, keywords: list, locations: list, credentials: dict, out_path: str, incl_path: str = None):
        self._root = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
        self._ledger = Ledger().scraper("glassdoor")

        self._chrome = Chrome(
            mode="undetected",
            options_args=["--disable-popup-blocking"],
            headless=False)
        self._files = Files()

        self._keywords = keywords
        self._locations = locations
        self._credentials = credentials
        self._out_path = out_path
        self._incl_path = incl_path or self._ledger["paths"]["files"]["temp_list"]

        self._load_data()

    def _load_data(self):
        self._scraping_info = self._files.read_file(self._ledger["paths"]["files"]["scraping_info"], route=True, default={})
        self._jobs_list = self._files.read_file(self._ledger["paths"]["files"]["jobs_list"], route=True, default={})
        self._jobs_hash = self._files.read_file(self._ledger["paths"]["files"]["jobs_hash"], route=True, default={})
        self._temp_list = self._files.read_file(self._incl_path, route=True, default=[])

    def _save_data(self):
        self._files.write_json(self._ledger["paths"]["files"]["scraping_info"], self._scraping_info)
        self._files.write_json(self._ledger["paths"]["files"]["jobs_list"], self._jobs_list)
        self._files.write_json(self._ledger["paths"]["files"]["jobs_hash"], self._jobs_hash)
        self._files.write_json(self._incl_path, self._temp_list)

    @staticmethod
    def _gen_hash(hash_input: str):
        return hashlib.sha256(hash_input.encode()).hexdigest()

    def _restart_driver(self):
        del self._chrome
        self._chrome = Chrome(
            mode="undetected",
            options_args=["--disable-popup-blocking"],
            headless=False)

    def _get_job_data(self, element, max_attempts=3):
        def get_overview_info():
            data = {}
            try:
                overview_elements = contents.find_all("div", {"class": ["JobDetails_overviewItem__cAsry"]})
                for ov_element in overview_elements:
                    try:
                        key = ov_element.find("span")
                        value = ov_element.find("div")
                        if key and value:
                            data["_".join(key.text.strip().lower().split(" "))] = value.text.strip()
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            return data

        def get_reviews_info():
            data = {}
            try:
                reviews_headlines = contents.find_all("span", {
                    "class": ["JobDetails_reviewConsLabel__rua2F", "JobDetails_reviewLabel__tm_4F"]})
                reviews_contents = contents.find_all("ul", {"class": ["JobDetails_reviewBlurbList__ZtUjH"]})
                for rh_element, rc_element in zip(reviews_headlines, reviews_contents):
                    try:
                        if rh_element:
                            value = "\n".join([value.text.strip() for value in rc_element.find_all("li")])
                            data["_".join(rh_element.text.strip().lower().split(" "))] = value
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            return data

        def get_ratings_info():
            data = {}
            try:
                ratings_detail_ulist = contents.find("ul", {"class": ["JobDetails_ratingTrendList__3G4DA"]})
                for rd_element in ratings_detail_ulist.find_all("li"):
                    try:
                        key = rd_element.find("span")
                        value = rd_element.find("div")
                        if key and value:
                            data["_".join(key.text.strip().lower().split(" "))] = value.text.strip()
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            return data

        def get_scores_info():
            data = {}
            try:
                ratings_scores_ulist = contents.find("ul", {"class": ["JobDetails_employerStatsDonuts__uWTLY"]})
                for rs_element in ratings_scores_ulist.find_all("li"):
                    try:
                        key = rs_element.find("span")
                        value = rs_element.find("svg")
                        if key and value:
                            data["_".join(key.text.strip().lower().split(" "))] = value.text.strip()
                        if not value:
                            ceo_name = rs_element.find("div", {"class": ["JobDetails_ceoTextWrapper__tvnKp"]})
                            if ceo_name:
                                data["ceo_name"] = ceo_name.text.strip()
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            return data

        try:
            WebDriverWait(self._chrome.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, f"li[data-jobid='{element.attrs["data-jobid"]}']"))
            ).click()
            time.sleep(random.uniform(2, 4))

            contents = self._chrome.get_soup().find("div", {"class": ["TwoColumnLayout_jobDetailsContainer__qyvJZ"]})
            info = {
                "company": contents.find("h4", {"class": ["heading_Heading__BqX5J heading_Subhead__Ip1aW"]}),
                "title": contents.find("h1", {"class": ["heading_Heading__BqX5J heading_Level1__soLZs"]}),
                "location": contents.find("div", {"class": ["JobDetails_location__mSg5h"]}),
                "details": contents.find("div", {
                    "class": ["JobDetails_jobDescription__uW_fK", "JobDetails_showHidden__C_FOA"]}),
                "rating": contents.find("div", {"class": ["RatingHeadline_sectionRatingScoreLeft__di1of"]}),
                "salary": contents.find("div", {"class": ["SalaryEstimate_salaryEstimateContainer__GkgnI"]}),
                "posted": element.find("div", {"data-test": "job-age"})
            }
            for key, value in info.items():
                info[key] = value.text.strip() if value is not None and isinstance(value, Tag) else "N/A"
            info["overview"] = get_overview_info()
            info["reviews"] = get_reviews_info()
            info["ratings"] = get_ratings_info()
            info["scores"] = get_scores_info()
        except Exception as e:
            self._close_job_alert_modal()
            return self._get_job_data(element, max_attempts - 1) if max_attempts > 0 else None
        return info

    def _fetch_list(self, keyword, location):
        status, soup = self._search_query(location, keyword)
        if not status:
            return {}

        elements = soup.find("div", {"class": ["JobsList_wrapper__EyUF6"]})
        for element in elements.find_all("li", {"data-test": "jobListing"}):
            url = element.find("a", {"data-test": "job-title"}).attrs["href"]
            url_hash = self._gen_hash(url)
            if url_hash not in self._temp_list:
                self._temp_list.append(url_hash)
            if url_hash in self._jobs_hash:
                continue
            job_data = self._get_job_data(element)
            if not job_data:
                continue

            job_hash = self._gen_hash(f"{job_data["title"]} at {job_data["company"]}")
            job_data.update({
                "url": url,
                "url_hash": url_hash,
                "job_hash": job_hash,
                "search_keyword": keyword,
                "search_location": location,
                "created_at": datetime.now(UTC).isoformat()
            })
            self._jobs_hash[url_hash] = job_hash
            self._jobs_list[job_hash] = job_data
            print(f"{job_data['title']} at {job_data['company']} in {job_data['location']} added to the list.")

    def fetch(self):
        self._sign_in()
        if "latest" not in self._scraping_info:
            self._scraping_info["latest"] = {}
        for location in self._locations:
            for keyword in self._keywords:
                if f"{keyword}-{location}" in self._scraping_info["latest"]:
                    latest_search = datetime.fromisoformat(self._scraping_info["latest"][f"{keyword}-{location}"])
                    if (datetime.now(UTC) - latest_search).total_seconds() < 172800:
                        print(f"Skipping '{keyword}' jobs in '{location}'.")
                        continue

                self._fetch_list(keyword, location)
                self._scraping_info["latest"][f"{keyword}-{location}"] = datetime.now(UTC).isoformat()
                self._save_data()
        return self.finalize()

    def finalize(self):
        del self._chrome

        jobs = {}
        for url_hash in self._temp_list:
            job_hash = self._jobs_hash.get(url_hash)
            if not job_hash:
                continue
            job_data = self._jobs_list[job_hash]
            job_hash_norm = self._gen_hash(f"{job_data['title']} at {job_data['company']}".lower())
            if job_hash_norm in jobs:
                if job_data["details"] == jobs[job_hash_norm]["details"]:
                    continue
            jobs[job_hash_norm] = job_data

        self._files.write_json(self._out_path, jobs)
        print(f"Jobs list saved to {self._out_path}.")

        return jobs

    def _sign_in(self, max_attempts=5):
        try:
            self._chrome.driver.get("https://www.glassdoor.ca")
            WebDriverWait(self._chrome.driver, 10).until(
                ec.element_to_be_clickable((By.ID, 'inlineUserEmail'))
            ).send_keys(self._credentials["email"])
            WebDriverWait(self._chrome.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="email-form-button"]'))
            ).click()
            WebDriverWait(self._chrome.driver, 10).until(
                ec.element_to_be_clickable((By.ID, 'inlineUserPassword'))
            ).send_keys(self._credentials["password"])
            sign_element = self._chrome.driver.find_element(By.NAME, 'authEmailForm')
            sign_element.find_element(By.XPATH, ".//button[.//span[text()='Sign in']]").click()
        except Exception as e:
            print(f"Trouble signing in: {e}")
            if max_attempts > 0:
                self._restart_driver()
                return self._sign_in()
            return False
        return True

    def _close_job_alert_modal(self):
        def check_if_present():
            try:
                WebDriverWait(self._chrome.driver, 1).until(
                    ec.visibility_of_element_located((By.CSS_SELECTOR, "button[data-test='job-alert-modal-close']")))
                return True
            except Exception as e:
                return False

        if not check_if_present():
            return False

        try:
            WebDriverWait(self._chrome.driver, 10).until(
                (ec.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='job-alert-modal-close']")))
            ).click()
            print(f"Job Alert Modal closed")
            return True
        except Exception as e:
            pass
        return False

    def _resolve_cloudflare_detection(self):
        if "Help Us Protect Glassdoor" in self._chrome.get_soup().text:
            print("Cloudflare detected. Resolving...")
            self._restart_driver()
            self._sign_in()
        return False

    def _scroll_down(self):
        def get_num_jobs():
            soup = self._chrome.get_soup()
            try:
                text = soup.find("div", {
                    "class": "SearchResultsHeader_searchResultsHeader__uK15O"
                }).text.replace(',', '')
                list_length = int(re.search(r"\d+", text).group())
                print(f"Found {list_length} jobs.")
                return list_length
            except Exception as ee:
                error = soup.find("h1", {"class": "ErrorPage_errorPageTitle__XtznY"})
                if error and error.text == 'No results found':
                    return 0
                print(f"Trouble finding the number of jobs: {ee}")
                return False

        def get_num_found():
            try:
                soup = self._chrome.get_soup()
                elements = soup.find("div", {"class": ["JobsList_wrapper__EyUF6"]})
                return len(elements.find_all("li", {"data-test": "jobListing"}))
            except Exception as e:
                print(f"Trouble finding the number of jobs found: {e}")
                return False

        time.sleep(random.uniform(2, 3))
        self._close_job_alert_modal()

        num_jobs = get_num_jobs()
        if num_jobs is False:
            return "Error"
        if num_jobs == 0:
            return False

        while True:
            num_found = get_num_found()
            if num_found is False:
                return "Error"
            if num_found == num_jobs:
                break

            time.sleep(random.uniform(2, 3))
            wait = WebDriverWait(self._chrome.driver, 10)
            try:
                load_more_button = wait.until(
                    ec.visibility_of_element_located((By.CSS_SELECTOR, "button[data-test='load-more']")))
                self._chrome.driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
                wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='load-more']")))
                time.sleep(random.uniform(1, 2))
                load_more_button.click()
            except Exception as e:
                if self._close_job_alert_modal():
                    continue
                if num_found == 0:
                    return False
                break
        return True

    def _search_query(self, location, keyword):
        time.sleep(random.uniform(2, 4))
        print(f"Searching for '{keyword}' jobs in '{location}'...")
        self._chrome.driver.get("https://www.glassdoor.ca/Job/index.htm")

        try:
            job_title_element = self._chrome.driver.find_element(By.ID, "searchBar-jobTitle")
            job_title_element.clear()
            job_title_element.send_keys(keyword)
            time.sleep(random.uniform(1, 2))

            job_location_element = self._chrome.driver.find_element(By.ID, "searchBar-location")
            job_location_element.clear()
            job_location_element.send_keys(location)
            time.sleep(random.uniform(1, 2))
            job_location_element.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Trouble searching for jobs: {e}")

        time.sleep(random.uniform(2, 4))
        if self._resolve_cloudflare_detection():
            return self._search_query(location, keyword)

        status = self._scroll_down()
        if status == "Error":
            return self._search_query(location, keyword)

        soup = self._chrome.get_soup()
        return status, soup


if __name__ == "__main__":
    from modules.data import Data

    data = Data("AmirMasoud Azadfar", "glassdoor", renew_descriptions=True)
    glassdoor = Glassdoor(
        keywords=data.preferences["roles"],
        locations=data.preferences["locations"],
        credentials=data.preferences["credentials"]["glassdoor"],
        out_path=data.paths["files"]["descriptions"],
        incl_path=data.paths["files"]["jobs_hash_idx"])
    # glassdoor.fetch()
    glassdoor.finalize()
