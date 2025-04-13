# 多功能程序（Multifunctional_Program）

---

### 程序简介&使用教程

- 该程序可以 **自动识别** ./funcs/ 下的文件夹并加载（./funcs/ 文件夹下的文件夹会被识别为功能模块）。
- 如何添加一个功能呢？这十分的简单。只需要在 **./funcs/ 文件夹** 下创建一个 **.py** 文件，然后按照以下格式编写：

```python
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
    └─__main__
            about.json
            commands.py
            create_new_module.py
            load_module_from_folder.py
            main.py
            print_help.py
```

- 整个项目文件夹内只有 ./run.py 能直接运行（默认情况下）。即 ./run.py 是整个程序的入口。

### commands.py 文件介绍

- `clear_screen()` 方法
  可以实现控制台清屏（Windows、macOS、GNU/Linux 通用）。
- `pause()` 方法
  可以实现回车键继续（Windows、macOS、GNU/Linux 通用），可以搭配 `clear_screen()` 食用。
- `print_title()` 方法
  可以打印功能名字，一般使用方式为 `print_title("<function-name>")`，其中 `<function-name>` 为程序文件夹的名字，如 ./funcs/__main__/main.py 中就使用了 `print_title("__main__")`。
- 使用前需要先引入该模块（`import funcs.addons.commands` 或 `from funcs.addons.commands import *`）。

### 添加参数
- 使用 `python ./run.py --help` 获取命令帮助。
```
用法：python ./run.py <command> <option>
也可直接运行 ./run.py
<command>
--help              获取命令参数帮助
--create-new-module 创建一个新的模块
                    <option>
                    dirname=...（此处 "..." 可以为任何值，它将会是最终在 ./funcs 下最终会展示出来的模块文件夹名）
                    funcname=...（此处 "..." 可以为任何值，它将会是在直接运行 ./run.py 时展示出来的模块名）
                    functype=function（此处 "function" 也可以是 "plugin"，若为 "plugin" 则在运行 ./run.py 时不会作为实用功能加载）
```
- 是的，可以用 `--create-new-module` 参数直接创建一个新的功能，而不必为程序的文件结构而纠结。
