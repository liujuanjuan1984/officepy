import os
import pytest
import sys


class TestCase:
    def test_dir(self):
        from officepy import Dir

        path = os.path.realpath(".")

        Dir(path).check()
        Dir(path).black()
        for i in Dir(path).search_files_by_types(".py"):
            print(i)

    def test_jsonfile(self):
        from officepy import JsonFile

        data = JsonFile("temp.json").read({})
        data.update({"hi": "hello"})
        JsonFile("temp.json").write(data)
        JsonFile("temp.json").rewrite()

    def test_update(self):
        """update local officepy to HEAD version"""
        from config import Config

        os.system(f"cd {Config.OFFICEPY_DIR}")
        os.system("git pull origin main")
        os.system("git pull origin main")
        os.system("git pull origin main")
        print(Config.BASE_DIR)
        print(Config.OFFICEPY_DIR)
