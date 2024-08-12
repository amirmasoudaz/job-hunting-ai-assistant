import asyncio
import json
import os
import shutil

import aiofiles
from docx import Document
import pandas as pd
import PyPDF2


class Files:
    def __init__(self, concurrent_operations: int = 100):
        self._semaphore = asyncio.Semaphore(concurrent_operations)

    @staticmethod
    def normalize_path(path: str) -> str:
        """
        Normalize a path.

        :param path: Path to normalize.
        :return: Normalized path.
        """
        prohibited = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
        for char in prohibited:
            path = path.replace(char, "_")

        return path

    @staticmethod
    def copy_file(src: str, dest: str) -> bool:
        """
        Copy a file from one location to another

        :param src: Source path of the file
        :param dest: Destination path of the file

        :return: None
        """
        try:
            shutil.copy2(src, dest)
            return True
        except Exception as e:
            return False

    @staticmethod
    def copy_dir(src: str, dest: str) -> None:
        """
        Copy a directory from one location to another

        :param src: Source path of the directory
        :param dest: Destination path of the directory

        :return: None
        """
        try:
            shutil.copytree(src, dest)
        except Exception as e:
            print(f"Error Copying Directory: {e}")

    @staticmethod
    def delete_file(path: str) -> bool:
        """
        Delete a file

        :param path: Path to the file
        :return: None
        """
        try:
            os.remove(path)
            return True
        except FileNotFoundError:
            return True
        except Exception as e:
            return False

    @staticmethod
    def delete_dir(path: str) -> bool:
        """
        Delete a directory

        :param path: Path to the directory
        :return: None
        """
        try:
            shutil.rmtree(path)
            return True
        except FileNotFoundError:
            return True
        except Exception as e:
            return False

    def read_files(self, path: str, dtype: str = "json", default=None) -> dict:
        """
        Read all files in a directory with a specific dtype

        :param path: Path to the directory
        :param dtype: Data type of the files to read  (json, txt, csv, etc.)
        :param default: Default value to return if file is not found

        :return: Dictionary of file contents with file name (without the dtype) as key and content as value
        """
        contents = {}
        if os.path.exists(path) and os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith(dtype):
                    ident = file.replace(f".{dtype}", "")

                    if dtype == "json":
                        contents[ident] = self.read_json(os.path.join(path, file), default=default)
                    elif dtype in ["csv", "xlsx", "pkl"]:
                        contents[ident] = self.read_df(os.path.join(path, file), dtype, default=default)
                    else:
                        contents[ident] = self.read_file(os.path.join(path, file), default=default)

        return contents

    async def read_files_async(self, path: str, dtype: str = "json", default=None) -> dict:
        """
        Read all files in a directory with a specific dtype asynchronously

        :param path: Path to the directory
        :param dtype: Data type of the files to read  (json, txt, etc.) [NOT SUPPORTED FOR DATAFRAMES]
        :param default: Default value to return if file is not found

        :return: Dictionary of file contents with file name (without the dtype) as key and content as value
        """
        tasks, idents = [], []
        if os.path.exists(path) and os.path.isdir(path):
            for file in os.listdir(path):
                if file.endswith(dtype):
                    idents.append(file.replace(f".{dtype}", "") if dtype != "all" else file)

                    if dtype == "json":
                        tasks.append(self.read_json_async(os.path.join(path, file), default=default))
                    else:
                        tasks.append(self.read_file_async(os.path.join(path, file), default=default))

        results = await asyncio.gather(*tasks)
        contents = {ident: content for ident, content in zip(idents, results)}

        return contents

    def write_files(self, path: str, contents: dict, dtype: str, encoding: str = "utf-8") -> None:
        """
        Write contents to a directory with a specific dtype

        :param path: Path to the directory
        :param contents: Dictionary of file contents with file name as key and content as value
        :param dtype: Data type of the files to write  (json, txt, csv, etc.)
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        if not os.path.exists(path):
            os.makedirs(path)

        for ident, content in contents.items():
            file_path = os.path.join(path, f"{ident}.{dtype}")
            if dtype in ["csv", "xlsx", "pkl"]:
                self.write_df(file_path, content, dtype)
            elif dtype == "json":
                self.write_json(file_path, content, encoding=encoding)
            else:
                self.write_file(file_path, content, encoding=encoding)

    async def write_files_async(self, path: str, contents: dict, dtype: str, encoding: str = "utf-8") -> None:
        """
        Write contents to a directory with a specific dtype asynchronously

        :param path: Path to the directory
        :param contents: Dictionary of file contents with file name as key and content as value
        :param dtype: Data type of the files to write  (json, txt, etc.) [NOT SUPPORTED FOR DATAFRAMES]
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        if not os.path.exists(path):
            os.makedirs(path)

        tasks = []
        for ident, content in contents.items():
            file_path = os.path.join(path, f"{ident}.{dtype}")
            if dtype == "json":
                tasks.append(self.write_json_async(file_path, content, encoding=encoding))
            else:
                tasks.append(self.write_file_async(file_path, content, encoding=encoding))

        await asyncio.gather(*tasks)

    def read_file(self, path: str, default=None, route=False) -> any:
        """
        Read a file

        :param path: Path to the file
        :param default: Default value to return if file is not found
        :param route: Route to the correct function

        :return: content
        """
        if route:
            dtype = path.split(".")[-1]
            if dtype == "json":
                return self.read_json(path, default=default)
            elif dtype in ["csv", "xlsx", "pkl"]:
                return self.read_df(path, dtype, default=default)
            elif dtype == "docx":
                return self.read_docx(path, default=default)
            elif dtype == "pdf":
                return self.read_pdf(path, default=default)
            else:
                return self.read_file(path, default=default, route=False)
        try:
            with open(path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return default

    async def read_file_async(self, path: str, default=None, route=False) -> any:
        """
        Read a file asynchronously

        :param path: Path to the file
        :param default: Default value to return if file is not found
        :param route: Route to the correct function

        :return: content
        """
        if route:
            dtype = path.split(".")[-1]
            if dtype == "json":
                return await self.read_json_async(path, default=default)
            elif dtype in ["csv", "xlsx", "pkl"]:
                return self.read_df(path, dtype, default=default)
            else:
                return await self.read_file_async(path, default=default, route=False)
        async with self._semaphore:
            try:
                async with aiofiles.open(path, "r") as file:
                    return await file.read()
            except FileNotFoundError:
                pass
            except Exception as e:
                print(f"Error Reading File: {e}")

            return default

    @staticmethod
    def write_file(path: str, data: any, mode: str = "w", encoding: str = "utf-8") -> None:
        """
        Write data to a file

        :param path: Path to the file
        :param data: Data to write
        :param mode: Method to use when writing the file (default: w)
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        if "b" in mode:
            encoding = None

        try:
            with open(path, mode, encoding=encoding) as file:
                file.write(data)
        except Exception as e:
            print(f"Error Writing File: {e}")

    async def write_file_async(self, path: str, data: str, encoding: str = "utf-8") -> None:
        """
        Write data to a file asynchronously

        :param path: Path to the file
        :param data: Data to write
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        async with self._semaphore:
            try:
                async with aiofiles.open(path, "w", encoding=encoding) as file:
                    await file.write(data)
            except Exception as e:
                print(f"Error Writing File: {e}")

    @staticmethod
    def read_json(path: str, default: dict or list = None) -> dict or list:
        """
        Read a JSON file

        :param path: Path to the JSON file
        :param default: Default value to return if file is not found or corrupted

        :return: JSON data
        """

        try:
            with open(path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    async def read_json_async(self, path: str, default: dict or list = None) -> dict or list:
        """
        Read a JSON file asynchronously

        :param path: Path to the JSON file
        :param default: Default value to return if file is not found or corrupted

        :return: JSON data
        """

        async with self._semaphore:
            try:
                async with aiofiles.open(path, "r") as file:
                    return json.loads(await file.read())
            except (FileNotFoundError, json.JSONDecodeError):
                default = {} if default is None else default
                await self.write_json_async(path, default, indent=4)

            return default

    @staticmethod
    def write_json(path: str, data: list or dict, indent: int = 4, encoding: str = "utf-8") -> None:
        """
        Write data to a JSON file

        :param path: Path to the JSON file
        :param data: Data to write
        :param indent: Indentation level
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        if not path.endswith(".json"):
            path += ".json"

        try:
            with open(path, "w", encoding=encoding) as file:
                json.dump(data, file, indent=indent)
        except Exception as e:
            print(f"Error Writing JSON: {e}")

    async def write_json_async(self, path: str, data: dict, indent: int = 4, encoding: str = "utf-8") -> None:
        """
        Write data to a JSON file asynchronously

        :param path: Path to the JSON file
        :param data: Data to write
        :param indent: Indentation level
        :param encoding: Encoding to use when writing the file (default: utf-8)

        :return: None
        """
        if not path.endswith(".json"):
            path += ".json"

        async with self._semaphore:
            try:
                async with aiofiles.open(path, "w", encoding=encoding) as file:
                    await file.write(json.dumps(data, indent=indent))
            except Exception as e:
                print(f"Error Writing JSON: {e}")

    @staticmethod
    def read_df(path: str, dtype: str = "csv", default=None) -> pd.DataFrame:
        """
        Read a dataframe from a file

        :param path: Path to the file
        :param dtype: Data type of the file  (csv, pkl, xlsx)
        :param default: Default value to return if file is not found

        :return: Pandas DataFrame
        """
        try:
            if dtype == "csv":
                return pd.read_csv(path)
            elif dtype == "pkl":
                return pd.read_pickle(path)
            elif dtype == "xlsx":
                return pd.read_excel(path)
            else:
                raise ValueError(f"Invalid Dataframe dtype: {dtype}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error: {e}")

        return default

    @staticmethod
    def write_df(path: str, data: pd.DataFrame, dtype: str = "csv") -> None:
        """
        Write a dataframe to a file

        :param path: Path to the file
        :param data: Pandas DataFrame
        :param dtype: Data type of the file  (csv, pkl, xlsx)

        :return: None
        """
        try:
            if dtype == "csv":
                data.to_csv(path, index=False)
            elif dtype == "pkl":
                data.to_pickle(path)
            elif dtype == "xlsx":
                data.to_excel(path, index=False)
            else:
                raise ValueError(f"Invalid Dataframe dtype: {dtype}")
        except Exception as e:
            print(f"Error Writing CSV: {e}")

    @staticmethod
    def read_docx(path: str, default=None) -> str:
        """
        Read a DOCX file
        :param path:  Path to the DOCX file
        :param default:  Default value to return if file is not found
        :return:  Text content of the DOCX file
        """
        try:
            return " ".join("\n".join([p.text for p in Document(path).paragraphs]).split())
        except FileNotFoundError:
            return default

    @staticmethod
    def read_pdf(path: str, join_doc: bool = False, default=None) -> str or list:
        """
        Read a PDF file
        :param path:  Path to the PDF file
        :param join_doc: Join a document (default: False)
        :param default:  Default value to return if file is not found
        :return:  Text content of the PDF file
        """
        try:
            document = []
            reader = PyPDF2.PdfReader(path)
            if not reader.pages:
                return default
            for page in reader.pages:
                document.append(page.extract_text())

            return " ".join("\n".join(document).split()) if join_doc else document
        except Exception as e:
            return default

    @staticmethod
    def write_pdf(path: str, data: str) -> None:
        """
        Write data to a PDF file
        :param path:  Path to the PDF file
        :param data:  Data to write
        :return:  None
        """
        try:
            with open(path, 'wb') as file:
                writer = PyPDF2.PdfWriter(file)
                writer.write(data)
        except Exception as e:
            print(f"Error Writing PDF: {e}")
