# 多功能程序（Multifunctional_Program）

---

### 程序简介&使用教程

- 该程序可以 **自动识别** ./funcs/ 下的 .py 文件并加载（./funcs/ 文件夹下的 .py 文件会被识别为功能模块）。
- 如何添加一个功能呢？这十分的简单。只需要在 **./funcs/文件夹** 下创建一个 **.py** 文件，然后按照以下格式编写：

```python
NAME = "这里是功能的名字，最后在运行main.py的时候会在主界面显示"
# 如果有import写到这
# 如果有其它类或函数写到这里
def run():
    # 这个函数是主要代码，主程序全往里写就行
```

- 写完之后可以运行 **./run.py**，没有意外的话可以成功加载，输入代号就可以选择；最后测试没问题就可以用了。
- 主程序使用 Windows 系统编写，macOS 与 GNU/Linux 大概也可以用。
- 本程序需要的最低 Python 环境为 **Python 3.6**（下载链接：[Python 官网](https://www.python.org/downloads "下载 Python 解释器（官方源）") / [阿里云镜像](https://mirrors.aliyun.com/python-release "下载 Python 解释器（阿里云镜像源）")），若运行不了的话考虑**升级 Python 解释器**。*这边建议用 Python 3.12 呢，主程序就用这版本写的，绝对错不了。*

### 默认文件结构

- 在没有任何功能的情况下，能确保程序正常运行的文件结构如下：

```
.
│  run.py
│
└─funcs
    └─addons
        │  commands.py
        │
        └─main
                load_modules.py
                main.py
```

- 整个项目文件夹内只有 ./run.py 能直接运行（默认情况下）。即 ./run.py 是整个程序的入口。

### commands.py 文件介绍

- `clear_screen()` 方法
  可以实现控制台清屏（Windows、macOS、GNU/Linux通用）。
- `pause()` 方法
  可以实现回车键继续（Windows、macOS、GNU/Linux通用），可以搭配 `clear_screen()` 食用。
- `print_title()` 方法
  可以打印功能名字，一般使用方式为 `print_title(NAME)`。
- 使用前需要先引入该模块（`import funcs.addons.commands` 或 `from funcs.addons.commands import *`）。

### Addons 目录

- 该目录旨在往里放入功能的附属程序与文件（如 davrkyybxi.py 中专门定义常量的 consts.py 放在 .\plugins\davrkyybxi\ 下）。
