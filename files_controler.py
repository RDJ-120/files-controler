import os
import shutil
from datetime import datetime

class PathError(Exception):
    pass

class FilePermissionError(Exception):
    pass


class Info:
    @staticmethod
    def help():
        print("""Information about the module

The module contains 7 main functions:

1. File.write(filepath, filename, text)
2. File.append(filepath, filename, text)
3. File.delete_content(filepath, filename)
4. File.stat(filepath, filename)
5. File.delete(filepath, filename)
6. File.copy(oldpath, newpath)
7. File.move(oldpath, newpath)
8. File.read(filepath, filename)
""")


class Path:
    @staticmethod
    def chdir(path):
        if os.path.exists(path):
            os.chdir(path)
        else:
            raise PathError("Path Not Found.")


class File:
    @staticmethod
    def read(filepath, filename):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)

        if not os.path.exists(full):
            raise FileNotFoundError(f"{filename} Not Found")

        with open(full, "r") as f:
            return f.read()


    @staticmethod
    def write(filepath, filename, text):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)
        with open(full, "w") as f:
            f.write(text)


    @staticmethod
    def append(filepath, filename, text):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)
        with open(full, "a") as f:
            f.write(text)


    @staticmethod
    def delete_content(filepath, filename):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)
        with open(full, "w") as f:
            f.write("")


    @staticmethod
    def stat(filepath, filename):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)

        if not os.path.exists(full):
            raise FileNotFoundError(f"{filename} Not Found")

        info = os.stat(full)
        size_kb = info.st_size / 1024
        last_edit = datetime.fromtimestamp(info.st_mtime)
        created = datetime.fromtimestamp(info.st_ctime)

        print(f"""
File Path:   {full}
Filename:    {filename}
Size:        {size_kb:.2f} KB
Created:     {created}
Last Edit:   {last_edit}
""")


    @staticmethod
    def delete(filepath, filename):
        if not os.path.exists(filepath):
            raise PathError(f"Path {filepath} Not Found")

        full = os.path.join(filepath, filename)

        if not os.path.exists(full):
            raise FileNotFoundError(f"{filename} Not Found")

        os.remove(full)


    @staticmethod
    def copy(oldpath, newpath):
        if not os.path.exists(oldpath):
            raise PathError(f"Source path {oldpath} Not Found")

        try:
            shutil.copy2(oldpath, newpath)
        except Exception as e:
            raise PermissionError(str(e))


    @staticmethod
    def move(oldpath, newpath):
        if not os.path.exists(oldpath):
            raise PathError(f"Source path {oldpath} Not Found")

        try:
            shutil.move(oldpath, newpath)
        except Exception as e:
            raise PermissionError(str(e))
