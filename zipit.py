import zipfile
import os
import datetime


def add_file(path, zf):
    for subpath in os.listdir(path):
        if subpath in not_dirname:
            continue
        subpath = os.path.join(path, subpath)
        print(subpath)
        if os.path.isfile(subpath):
            if not subpath.endswith(not_filetype):
                zf.write(subpath)
        elif os.path.isdir(subpath):
            zf.write(subpath)
            add_file(subpath, zf)


def zip_compress(path, to_zipfile):
    zf = zipfile.ZipFile(to_zipfile, mode="a")
    add_file(path, zf)
    zf.close()


from_paths = [r"D:\Jupyter\officepy", r"D:\Jupyter\rumpy", r"D:\Jupyter\seedstore2"]
to_path = r"D:\Jupyter\docs\rum-app\app"

not_dirname = [
    "__pycache__",
    ".pytest_cache",
    ".git",
    "tests",
    "examples",
    "database",
    "Makefile",
    "docs",
]
not_filetype = (".7z", ".db", ".zip")


to_zipfile = os.path.join(to_path, f"srcipts_{datetime.date.today()}.zip")
if os.path.exists(to_zipfile):
    to_zipfile = to_zipfile.replace(".zip", "1.zip")
print(to_zipfile)
for path in from_paths:
    zip_compress(path, to_zipfile)
