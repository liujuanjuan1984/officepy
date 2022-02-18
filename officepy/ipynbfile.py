from .myfile import File
from .jsonfile import JsonFile


class IpynbFile(JsonFile):
    def to_md(self, markdown_filepath=None, is_output=False):
        """
        output ipynbfile to markdown file
        is_output: 是否导出输出信息
        """

        if not self.filepath.endswith(".ipynb"):
            raise ValueError(f"{filepath}\n not .ipynb file")

        data = self.read({})
        try:
            language = data["metadata"]["language_info"]["name"]
        except:
            language = "text"

        datastr = ""
        for cell in data.get("cells") or []:
            if cell["cell_type"] == "code":
                datastr += f"```{language}\n" + "".join(cell["source"]) + "\n```\n\n"
                if is_output:  # 运行结果导出不够全面完整
                    if len(cell["outputs"]) > 0:
                        outputs = "**Returns**:\n\n"
                        for j in cell["outputs"]:
                            if j["output_type"] == "execute_result":
                                outputs += "".join(j["data"]["text/plain"]) + "\n\n"
                            elif j["output_type"] == "error":
                                outputs += "**Error**: " + j["evalue"] + "\n\n"
                            else:
                                print(j["output_type"])
                        datastr += outputs
            else:
                datastr += "".join(cell["source"]) + "\n\n"

        markdown_filepath = markdown_filepath or self.filepath.replace(".ipynb", ".md")
        File(markdown_filepath).write(datastr)
