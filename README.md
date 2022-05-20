# officy

common python code for office use. like dir,file,etc.

### Install

```sh
pip install officy
pip install -r requirements.txt
```

### How to use?

```py
from officy import Dir,JsonFile
Dir(".").black()
JsonFile("temp.json").read({})
```

### Code Format

Install:

```bash
pip install black
pip install isort
```

Format:

```bash
isort .
black -l 80 -t py37 -t py38 -t py39 -t py310 .
black -l 120 -t py37 -t py38 -t py39 -t py310 .
```

### Version

tool: [bumpversion](https://github.com/peritus/bumpversion)

config: [.bumpversion.cfg](.bumpversion.cfg)


1. bugfix: `bumpversion patch`

2. feature: `bumpversion minor`

3. breaking change: `bumpversion major`


```bash
git push origin master --tags
```
