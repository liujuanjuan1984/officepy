import os
import pytest
import sys


from officepy import *


class TestCase:
    def test_dir(self):
        path = os.path.realpath(".")
        Dir(path).check()
        Dir(path).black()
        for i in Dir(path).search_files_by_types(".py"):
            print(i)

    def test_jsonfile(self):
        data = JsonFile("temp.json").read({})
        data.update({"hi": "hello"})
        JsonFile("temp.json").write(data)
        JsonFile("temp.json").rewrite()
