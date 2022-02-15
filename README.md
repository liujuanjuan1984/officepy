# officepy

common python code for office use. like dir,file,etc.

办公用途的常用 python 代码，比较多涉及到文本、文件、文件夹、网页等。

## 安装使用

目前 `officepy` 没有采用 pip 等发布，所以不支持 `pip install officepy`。

如果您有需要，可以 clone 到本地，比如，在 `/work-space>` 下执行 ```git clone https://github.com/liujuanjuan1984/officepy.git```。

完成后，`cd officepy` 后所在目录/路径，请添加到 `PYTHONPATH` 环境变量中。

### 检查是否设置成功

检查 officepy 的本地路径是否在下述输出结果中。

```py
import sys
print(sys.path)
```

### 导入方式：

```py
from officepy import Dir,JsonFile
```


### 测试+ reformat：

```sh
pytest .\tests\
```

### 安装依赖：

```sh
pip install -r requirements.txt
```