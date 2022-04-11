import os
import pytest
import sys


class TestCase:
    def test_dir(self):
        from officy import Dir

        path = os.path.realpath(".")

        Dir(path).check()
        Dir(path).black()
        pys = Dir(path).search_files_by_types(".py")
        print(pys)

    def test_file(self):
        from officy import File
        from officy import IpynbFile

        notes_dir = os.path.join(os.path.dirname(__file__), "..", "notes")

        xfile = os.path.join(notes_dir, "Python_requests_examples.md")
        yfile = os.path.join(notes_dir, "Python_requests_examples.ipynb")
        data = File(xfile).read()
        File(xfile).write(data)
        data = File(xfile).readlines()
        File(xfile).writelines(data)

        File(xfile).zh_format()
        File(xfile).quote_json_format()

        # File(xfile).change_filetype(".md", ".txt")
        IpynbFile(yfile).to_md()

        # File(xfile).copy_file_to_other_type(".md", ".log")

        print(File("__init__.py").size())

    def test_jsonfile(self):
        from officy import JsonFile

        data = JsonFile("temp.json").read({})
        data.update({"hi": "hello"})
        JsonFile("temp.json").write(data)
        JsonFile("temp.json").rewrite()

    def test_img(self):
        """update local officy to HEAD version"""
        from officy import Img

        Img()

    def test_stime(self):
        from officy import Stime
        import datetime

        Stime.ts2datetime(1644992740511809600)
        Stime.ts2datetime(1644992740511809)
        Stime.ts2datetime(1644992740511)
        Stime.ts2datetime(1644992740)

        rlt = Stime.days_later("2021-01-01", 1)
        rlt = Stime.days_later(datetime.datetime.now(), 1)
        rlt = Stime.days_later(datetime.date.today(), 1)
