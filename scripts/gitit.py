import os
from officy import File


def main():
    reponames = ["officy", "seeds", "rumpy", "quorum_binary", "coin_price"]

    lines = []
    this_dir = os.path.dirname(__file__)
    home_dir = os.path.dirname(os.path.dirname(this_dir))

    for name in reponames:
        this_repo = os.path.join(home_dir, name)
        if os.path.exists(this_repo):
            line = "git pull origin master\n"
            lines.extend([f"cd {this_repo}\n", line * 3])
        else:
            line = f"git clone https://github.com/liujuanjuan1984/{name}\n"
            lines.extend([f"cd {home_dir}\n", line * 3])

    lines.append(f"cd {home_dir}\n")
    batfile = os.path.join(this_dir, "temp_git_it.bat")
    File(batfile).writelines(lines)


if __name__ == "__main__":
    main()
