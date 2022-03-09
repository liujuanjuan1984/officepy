import os
from officepy import File

reponames = ["officepy", "seeds", "rumpy", "quorum_binary"]

lines = []
this_dir = os.path.dirname(__file__)
home_dir = os.path.dirname(os.path.dirname(this_dir))


def clone():
    for name in reponames:
        line = f"git clone https://github.com/liujuanjuan1984/{name}\n"
        lines.append(line * 5)
        lines.append("\n")


def pull():
    for name in reponames:
        line = f"cd {os.path.join(home_dir,name)}\n"
        lines.append(line)
        lines.append("git pull origin master\n" * 5)
        lines.append("\n")


# clone()
pull()
batfile = os.path.join(os.path.dirname(__file__), "gitit.bat")
File(batfile).writelines(lines)
