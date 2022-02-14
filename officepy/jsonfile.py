import os
import json
import datetime


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, time):
            return obj.__str__()
        else:
            return super(NpEncoder, self).default(obj)


class JsonFile:
    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def data(self):
        return self.read()

    def read(self, nulldata=[]):
        if not os.path.exists(self.filepath):
            return nulldata

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise ValueError(f"{self.filepath}\n{e}")

    def write(self, data, indent=1, is_cover=True):

        filepath = self.filepath
        if os.path.exists(self.filepath) and is_cover == False:
            filepath += f"_{datetime.date.today()}_temp.json"

        with open(filepath, "w", encoding="utf-8") as f:
            try:
                json.dump(data, f, indent=indent, sort_keys=False, ensure_ascii=False)
            except:
                json.dump(
                    filedata,
                    __f,
                    indent=indent,
                    sort_keys=False,
                    ensure_ascii=False,
                    cls=MyEncoder,
                )

    def rewrite(self):
        self.write(self.read())
