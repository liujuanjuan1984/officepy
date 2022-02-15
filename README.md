# officepy

common python code for office use. like dir,file,etc.

办公用途的常用 python 代码，比较多涉及到文本、文件、文件夹、网页等。

### 安装使用

目前 `officepy` 还没有采用 pip 等发布，所以还不支持 `pip install officepy`。如果您有需要，可以在本地的 Python 路径下安装。

即在 `/Python/Python310/lib/site-packages>` 下执行：

```sh

git clone https://github.com/liujuanjuan1984/officepy.git

```

导入方式：

```py

from officepy.officepy import Dir,JsonFile

```

### 测试+ reformat：

```sh

pytest .\tests\

```

### 安装依赖：

```sh
pip install -r requirements.txt
```