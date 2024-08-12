import os

from dotenv import load_dotenv, find_dotenv

from tools.tree import Tree
from tools.singleton import Singleton


class Ledger(metaclass=Singleton):
    tree = Tree(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self):
        self._scraper = {}
        self._data = {}
        self._analyzer = None
        self._logger = None

    @staticmethod
    def _get_env_variable(key, default=None, required=False, var_type=None):
        var_type = var_type or str
        value = os.environ.get(key, default)
        if required and value is None:
            raise EnvironmentError(f"Missing required environment variable: {key}")
        if value is not None and var_type != str:
            if var_type == bool:
                value = True if value.lower() in ["true", "1"] else False
            else:
                try:
                    value = var_type(value)
                except ValueError:
                    raise ValueError(f"Environment variable {key} must be of type {var_type.__name__}")
        return value

    @staticmethod
    def prepare_dirs(base_dir: str, dir_names: list, exclude_mkdir: list = None):
        dirs = {
            dir_name: os.path.join(base_dir, dir_name)
            for dir_name in dir_names
        }
        for path in dirs.values():
            if exclude_mkdir and path in exclude_mkdir:
                continue
            os.makedirs(path, exist_ok=True)
        return dirs

    @property
    def logger(self):
        if self._logger is None:
            if not load_dotenv(find_dotenv("logging.env", usecwd=True)):
                print("Logging environment file not found.")
            self._logger = {
                "path": self.tree.get_path("dir_logging"),
                "level": self._get_env_variable("LEVEL"),
                "max_bytes": self._get_env_variable("FILE_MAX_BYTES", var_type=int),
                "backup_count": self._get_env_variable("FILE_BACKUP_COUNT", var_type=int)
            }
            os.makedirs(self._logger["path"], exist_ok=True)
        return self._logger.copy()

    @property
    def analyzer(self):
        if self._analyzer is None:
            if not load_dotenv(find_dotenv("analyzer.env", usecwd=True)):
                print("Analyzer environment file not found.")
            self._analyzer = {
                "modes": {
                    "customization": self._get_env_variable("APP_CUSTOMIZATION", var_type=bool),
                    "reprocessing": self._get_env_variable("APP_REPROCESSING", var_type=bool),
                    "eco_mode": self._get_env_variable("ECO_MODE_ANALYSIS", var_type=bool),
                    "categorization": self._get_env_variable("APP_CATEGORIZATION", var_type=bool),
                    "role_compatibility": self._get_env_variable("ROLE_COMPATIBILITY", var_type=bool),
                },
                "cs_thr": {
                    "role": self._get_env_variable("ROLE_COMP_SCORE_THRESHOLD", var_type=int),
                    "app": self._get_env_variable("APP_COMP_SCORE_THRESHOLD", var_type=int),
                    "match": self._get_env_variable("MATCH_COMP_SCORE_THRESHOLD", var_type=int)
                },
                "match_weights": {
                    "role": self._get_env_variable("ROLE_MATCH_COMP_WEIGHT", var_type=float),
                    "app": self._get_env_variable("APP_MATCH_COMP_WEIGHT", var_type=float),
                },
                "models": {
                    "embeddings": self._get_env_variable("EMBEDDINGS_GPT_MODEL"),
                    "efficient": self._get_env_variable("EFFICIENT_GPT_MODEL"),
                    "proficient": self._get_env_variable("PROFICIENT_GPT_MODEL"),
                }
            }
        return self._analyzer.copy()

    def scraper(self, platform: str):
        platform = platform.lower()
        if not self._scraper.get(platform):
            tree = self.tree.mod(PLATFORM=platform)
            self._scraper[platform] = {
                "platform": platform,
                "paths": {
                    "files": {
                        "jobs_list": self.tree.get_path(f"file_jobs_list_{platform}", tree=tree),
                        "jobs_hash": self.tree.get_path(f"file_jobs_hash_{platform}", tree=tree),
                        "temp_list": self.tree.get_path(f"file_temp_list_{platform}", tree=tree),
                        "scraping_info": self.tree.get_path(f"file_scraping_info_{platform}", tree=tree)
                    }
                }
            }
        return self._scraper[platform].copy()

    def data(self, user_name: str, platform: str = None):
        user_name = "-".join(user_name.lower().split())
        platform = platform.lower()
        if not self._data.get(user_name):
            if not load_dotenv(find_dotenv("data.env", usecwd=True)):
                print("Data environment file not found.")

            tree = self.tree.mod(USERNAME=user_name, PLATFORM=platform)
            resume_dir = self.tree.get_path(desc="dir_resume", tree=tree)
            self._data[user_name] = {
                "name": user_name,
                "models": {
                    "embeddings": self._get_env_variable("EMBEDDINGS_GPT_MODEL"),
                    "completions": self._get_env_variable("COMPLETIONS_GPT_MODEL"),
                },
                "paths": {
                    "dirs": {
                        "personal": self.tree.get_path("dir_personal", tree=tree),
                        "resume": self.tree.get_path("dir_resume", tree=tree),
                        "applications": self.tree.get_path(f"dir_applications_{platform}", tree=tree)
                    },
                    "files": {
                        "biography": self.tree.get_path("file_biography", tree=tree),
                        "preferences": self.tree.get_path("file_preferences", tree=tree),
                        "descriptions": self.tree.get_path(f"file_descriptions_{platform}", tree=tree),
                        "jobs_hash_idx": self.tree.get_path(f"file_jobs_hash_idx_{platform}", tree=tree),
                        "resume": {
                            "raw": os.path.join(resume_dir, "raw.txt"),
                            "json": os.path.join(resume_dir, "resume.json"),
                            "md": os.path.join(resume_dir, "sections.json"),
                            "text": os.path.join(resume_dir, "resume.md"),
                            "repl": os.path.join(resume_dir, "replica.txt")
                        }
                    }
                }
            }
        return self._data[user_name].copy()
