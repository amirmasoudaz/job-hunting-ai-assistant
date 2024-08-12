import os
import subprocess
import time

from bs4 import BeautifulSoup
from selenium import webdriver as dc
import undetected_chromedriver as uc


class WebDriver:
    def __init__(self, headless: bool = False, options_args: list = None, experimental_args: list = None):
        self.headless = headless
        self.options_args = options_args or []
        self.experimental_args = experimental_args or []

    def _set_options(self, options):
        if self.options_args:
            for arg in self.options_args:
                options.add_argument(arg)
        if "--headless" not in self.options_args and self.headless:
            options.headless = True

        if self.experimental_args:
            for arg in self.experimental_args:
                options.add_experimental_option(arg[0], arg[1])

        return options


class UndetectedChromeDriver(WebDriver):
    _options_args = [
        "--auto-open-devtools-for-tabs"
    ]

    def __init__(self, headless: bool = False, options_args: list = None, experimental_args: list = None):
        options_args = [] if not options_args else options_args
        super().__init__(headless, options_args + self._options_args, experimental_args)
        options = self._set_options(uc.ChromeOptions())
        self.driver = uc.Chrome(use_subprocess=True, options=options)


class DetectedChromeDriver(WebDriver):
    def __init__(self, headless: bool = False, options_args: list = None, experimental_args: list = None):
        super().__init__(headless, options_args, experimental_args)
        options = self._set_options(dc.ChromeOptions())
        self.driver = dc.Chrome(options=options)


class Chrome:
    _drivers = {
        "undetected": UndetectedChromeDriver,
        "default": DetectedChromeDriver
    }

    def __init__(
            self,
            mode: str = "default",
            headless: bool = False,
            options_args: list = None,
            experimental_args: list = None
    ):
        _instance = self._drivers.get(mode, self._drivers["default"])
        _instance = _instance(headless, options_args, experimental_args)
        self.driver = _instance.driver

    def __del__(self):
        def kill_process(name):
            try:
                if os.name == "nt":
                    result = subprocess.run(["tasklist", "/fi", f"imagename eq {name}"], capture_output=True, text=True)
                    if name in result.stdout:
                        subprocess.run(["taskkill", "/f", "/im", name], stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL)
                else:
                    pass
            except Exception as e:
                print(f"An error occurred: {e}")

        self.driver.quit()
        kill_process("chrome.exe")

    def open_new_tab(self) -> str:
        self.driver.execute_script("window.open('');")
        return self.driver.window_handles[-1]

    def close_tab(self, tab: str):
        self.driver.switch_to.window(tab)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_soup(self):
        return BeautifulSoup(self.get_source(), "html.parser")

    def get_source(self):
        return self.driver.page_source

    def fetch(self, url: str, dtype: str or None = None, delay: float = 0.0) -> BeautifulSoup or str or None:
        """
        Fetch data from the given URL.
        :param url: The URL to fetch
        :param dtype: The type of data to return. Options -> ["soup", "source", None]
        :param delay:  The delay to wait before returning the data
        :return:
        """
        self.driver.get(url)
        if delay:
            time.sleep(delay)
        if not dtype:
            return
        elif dtype == "soup":
            return self.get_soup()
        elif dtype == "source":
            return self.get_source()

    def find_xpath(self, xpath: str):
        return self.driver.find_element_by_xpath(xpath)

    def execute_script(self, script: str, element: dc or uc or None = None, delay: float = 0.0, click: bool = False):
        self.driver.execute_script(script, element)
        time.sleep(delay)
        if click:
            element.click()
        return element
