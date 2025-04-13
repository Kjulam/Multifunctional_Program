import os

def print_help():
    print(f"用法：python .{"\\" if os.name == "nt" else "/"}run.py <command> <option>")
    print(f"也可直接运行 .{"\\" if os.name == "nt" else "/"}run.py")
    print("<command>")
    print(f"--help {" " * 12} 获取命令参数帮助")
    print("--create-new-module 创建一个新的模块")
    print(f"{" " * 19} <option>")
    print(f"{" " * 19} dirname=...（此处 \"...\" 可以为任何值，它将会是最终在 .{"\\" if os.name == "nt" else "/"}funcs 下最终会展示出来的模块文件夹名）")
    print(f"{" " * 19} funcname=...（此处 \"...\" 可以为任何值，它将会是在直接运行 .{"\\" if os.name == "nt" else "/"}run.py 时展示出来的模块名）")
    print(f"{" " * 19} functype=function（此处 \"function\" 也可以是 \"plugin\"，若为 \"plugin\" 则在运行 .{"\\" if os.name == "nt" else "/"}run.py 时不会作为实用功能加载）")

