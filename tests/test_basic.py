import os
import pytest
import sys


class TestCase:
    def test_dir(self):
        from officepy import Dir

        path = os.path.realpath(".")

        Dir(path).check()
        Dir(path).black()
        pys = Dir(path).search_files_by_types(".py")
        print(pys)

    def test_file(self):
        from officepy import File

        data = File("temp.json").read()
        File("temp.json").write(data)
        data = File("temp.json").readlines()
        File("temp.json").writelines(data)

    def test_jsonfile(self):
        from officepy import JsonFile

        data = JsonFile("temp.json").read({})
        data.update({"hi": "hello"})
        JsonFile("temp.json").write(data)
        JsonFile("temp.json").rewrite()

    def test_img(self):
        """update local officepy to HEAD version"""
        from officepy import Img

        Img()

    def test_stime(self):
        from officepy import Stime

        Stime().ts2datetime(1644992740511809600)

    def test_ipynbfile(self):
        """update local officepy to HEAD version"""
        from officepy import IpynbFile

        filepath = (
            r"D:\Jupyter\my_repos\common_python_code\Python_requests_examples.ipynb"
        )
        IpynbFile(filepath).to_md()
