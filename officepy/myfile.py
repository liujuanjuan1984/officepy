import json
import os
import re
from .jsonfile import JsonFile


class File:
    """文件"""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            filedata = f.read()
        return filedata

    def write(self, filedata, mode="w", is_print=True):
        with open(self.filepath, mode, encoding="utf-8") as f:
            f.write(filedata)
        if is_print:
            print(self.filepath, f"mode:{mode} write done.")

    def readlines(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return lines

    def writelines(self, lines, mode="w", is_print=True):
        with open(self.filepath, mode, encoding="utf-8") as f:
            f.writelines(lines)
        if is_print:
            print(self.filepath, f"mode:{mode} writelines done.")

    def change_filetype(self, fromtype, totype):
        """修改文件类型，会直接覆盖原文件"""
        if self.filepath.endswith(fromtype):
            af = self.filepath[: -len(fromtype)] + totype
            os.rename(self.filepath, af)
            return af
        return print(self.filepath, f"文件类型不是 {fromtype}，无法修改")

    def copy_file_to_other_type(self, fromtype, totype, is_cover=True):
        """修改文件类型，is_cover 是否覆盖已存在的文件"""
        if self.filepath.endswith(fromtype):
            bf = self.filepath
            af = bf[: -len(fromtype)] + totype
            if os.path.exists(af):
                if not is_cover:
                    return print(af, f"文件已存在，指定 is_cover 为 False 可覆盖")
                os.remove(af)
            os.system(f'copy "{bf}" "{af}"')
            return af
        return print(self.filepath, f"文件类型不是 {fromtype}，无法修改")

    def run_batgit(self, gitclis=None):
        """把命令行文本写文件并运行"""
        if not self.filepath.endswith(".bat"):
            return print("文件类型不符")
        if gitclis == None:
            gitclis = self.readlines()
        elif type(gitclis) != list:
            return print("请提供列表形式的命令行")
        else:
            self.writelines(gitclis)
        os.system(self.filepath)

    def zh_format(self):
        """中文排版优化"""
        data = self.read()
        data = self.zh_format_text(data)
        self.write(data)

    @classmethod
    def zh_format_text(cls, data):
        """中文排版优化"""

        # 中文和英文、数字之间应有空格
        data = re.sub(r"([\u4e00-\u9fa5])([\da-zA-Z])", r"\1 \2", data)
        data = re.sub(r"([\da-zA-Z])([\u4e00-\u9fa5])", r"\1 \2", data)

        # 多个换行，改为单个换行
        data = re.sub(r"\n{3,}", r"\n\n", data)

        # 文件首尾的多余换行
        data = re.sub(r"^[\n ]+", r"", data)
        data = re.sub(r"[\n ]+$", r"", data)
        return data

    def quote_json_format(self):
        """对 markdown 文件中所引用的 json 数据予以规范排版"""

        data = self.read()

        tp = r"\n```json\n+([\s\S]+?)```"
        rs = re.findall(tp, data)
        for i in rs:
            try:
                ix = json.loads(i)
                JsonFile("temp.json").write(ix, indent=4, is_print=False)
                ix = File("temp.json").read()
                data = data.replace(i, str(ix).replace("'", '"') + "\n")
            except Exception as e:
                print(i)
                print(e)
        self.write(data)
        self.zh_format()
