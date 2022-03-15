import os
from officepy import File


def main():
    reponames = ["officepy", "seeds", "rumpy", "quorum_binary", "coin_price"]

    lines = []
    this_dir = os.path.dirname(__file__)
    home_dir = os.path.dirname(os.path.dirname(this_dir))

    for name in reponames:
        this_repo = os.path.join(home_dir, name)
        if os.path.exists(this_repo):
            line = f"cd {this_repo}\n"
            lines.append(line)
            lines.append("git pull origin master\n" * 5)
            lines.append("\n")
        else:
            line = f"git clone https://github.com/liujuanjuan1984/{name}\n"
        lines.append(line * 5)
        lines.append("\n")

    batfile = os.path.join(os.path.dirname(__file__), "gitit.bat")
    File(batfile).writelines(lines)


if __name__ == "__main__":
    main()
