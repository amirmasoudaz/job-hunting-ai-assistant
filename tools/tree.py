import json
import os
import re


class Tree:
    tree = [
        {
            "parent": "",
            "desc": "dir_root",
            "children": [
                {
                    "parent": "data",
                    "desc": "dir_data",
                    "children": [
                        {
                            "parent": "profiles",
                            "desc": "dir_profiles",
                            "children": [
                                {
                                    "parent": "<USERNAME>",
                                    "desc": "dir_applicant",
                                    "children": [
                                        {
                                            "parent": "personal",
                                            "desc": "dir_personal",
                                            "children": [
                                                {
                                                    "parent": "biography.txt",
                                                    "desc": "file_biography",
                                                    "dtype": "txt"
                                                },
                                                {
                                                    "parent": "preferences.json",
                                                    "desc": "file_preferences",
                                                    "dtype": "json"
                                                }
                                            ]
                                        },
                                        {
                                            "parent": "resume",
                                            "desc": "dir_resume",
                                            "children": []
                                        },
                                        {
                                            "parent": "templates",
                                            "desc": "dir_templates",
                                            "children": [
                                                {
                                                    "parent": "resume",
                                                    "desc": "dir_template_resume",
                                                    "children": [
                                                        {
                                                            "parent": "template.html",
                                                            "desc": "file_template_resume",
                                                            "dtype": "html"
                                                        },
                                                        {
                                                            "parent": "styles.css",
                                                            "desc": "file_template_resume_styles",
                                                            "dtype": "css"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "parent": "letter",
                                                    "desc": "dir_template_letter",
                                                    "children": [
                                                        {
                                                            "parent": "template.docx",
                                                            "desc": "file_template_letter",
                                                            "dtype": "docx"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "parent": "email",
                                                    "desc": "dir_template_email",
                                                    "children": [
                                                        {
                                                            "parent": "template.txt",
                                                            "desc": "file_template_email",
                                                            "dtype": "txt"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "parent": "applications",
                                            "desc": "dir_applications",
                                            "children": [
                                                {
                                                    "parent": "<PLATFORM>",
                                                    "desc": "dir_applications_<PLATFORM>",
                                                    "children": []
                                                }
                                            ]
                                        },
                                        {
                                            "parent": "descriptions",
                                            "desc": "dir_descriptions",
                                            "children": [
                                                {
                                                    "parent": "descriptions_<PLATFORM>.json",
                                                    "desc": "file_descriptions_<PLATFORM>",
                                                    "dtype": "json"
                                                },
                                                {
                                                    "parent": "jobs_hash_idx_<PLATFORM>.json",
                                                    "desc": "file_jobs_hash_idx_<PLATFORM>",
                                                    "dtype": "json"
                                                }
                                            ]
                                        },
                                    ]
                                }
                            ]
                        },
                        {
                            "parent": "scrapers",
                            "desc": "dir_scrapers",
                            "children": [
                                {
                                    "parent": "<PLATFORM>",
                                    "desc": "dir_scraper_<PLATFORM>",
                                    "children": [
                                        {
                                            "parent": "jobs_list.json",
                                            "desc": "file_jobs_list_<PLATFORM>",
                                            "dtype": "json"
                                        },
                                        {
                                            "parent": "jobs_hash.json",
                                            "desc": "file_jobs_hash_<PLATFORM>",
                                            "dtype": "json"
                                        },
                                        {
                                            "parent": "scraping_info.json",
                                            "desc": "file_scraping_info_<PLATFORM>",
                                            "dtype": "json"
                                        },
                                        {
                                            "parent": "temp_list.json",
                                            "desc": "file_temp_list_<PLATFORM>",
                                            "dtype": "json"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "parent": "categories_index.pkl",
                            "desc": "file_categories_index",
                            "dtype": "pkl"
                        }
                    ]
                },
                {
                    "parent": "backlogs",
                    "desc": "dir_logging",
                    "children": []
                }
            ]
        }
    ]

    def __init__(self, root: str):
        self.tree = self.init(parent=root, tree=self.tree)
        self.make(self.tree)

    def init(self, parent: str, tree: list) -> list:
        for node in tree:
            node["parent"] = os.path.join(parent, node["parent"])
            if node.get("children"):
                self.init(node["parent"], node["children"])
        return tree

    def mod(self, **kwargs) -> list:
        tree_str = json.dumps(self.tree)
        for key, value in kwargs.items():
            if not value:
                continue
            tree_str = tree_str.replace(f"<{key}>", value)
        tree = json.loads(tree_str)
        self.make(tree)
        return tree

    def get_path(self, desc: str, tree: list = None) -> str:
        if not tree:
            return self.get_path(desc, self.tree)

        for node in tree:
            if node["desc"] == desc:
                return node["parent"]
            if node.get("children"):
                path = self.get_path(desc, node["children"])
                if path:
                    return path
        return ""

    def get_children(self, desc: str, tree: list = None) -> str or None:
        if not tree:
            return self.get_children(desc, self.tree)

        for node in tree:
            if node["desc"] == desc:
                return node["children"]
            if node.get("children"):
                return self.get_children(desc, node["children"])

    def make(self, tree: list) -> None:
        for node in tree:
            if not node.get("dtype") and not re.compile(r'<[^>]+>').search(node["parent"]):
                os.makedirs(node["parent"], exist_ok=True)
            if node.get("children"):
                self.make(node["children"])

    def add_child(self, tree: list, parent_desc: str, child: str, child_desc: str, dtype: str = None) -> None:
        for node in tree:
            if node["desc"] == parent_desc:
                child_path = os.path.join(node["parent"], child)
                if dtype:
                    node["children"].append({"parent": child_path, "desc": child_desc, "dtype": dtype})
                else:
                    node["children"].append({"parent": child_path, "desc": child_desc, "children": []})
                return self.make(node["children"])

            if node.get("children"):
                self.add_child(node["children"], parent_desc, child, child_desc, dtype)
