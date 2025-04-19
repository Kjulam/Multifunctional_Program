import re, os

def create_new_module(passedin_commands: list):
    dirname = None
    funcname = None
    functype = None

    for item in passedin_commands:
        if re.search(r"^dirname=.+$", item) and (passedin_commands.index(item) > passedin_commands.index("--create-new-module")):
            dirname = item.split("=")[1]
        elif re.search(r"^funcname=.+$", item) and (passedin_commands.index(item) > passedin_commands.index("--create-new-module")):
            funcname = item.split("=")[1]
        elif re.search(r"^functype=.+$", item) and (passedin_commands.index(item) > passedin_commands.index("--create-new-module")):
            if item.split("=")[1] == "function" or item.split("=")[1] == "plugin":
                functype = item.split("=")[1]
            else:
                print("错误：\"functype\" 参数只能有 \"function\" 或 \"plugin\" 两种属性。")
                return 1

    if dirname is None:
        print("错误：未传入参数 \"dirname=\"。")
        print("请使用 --help 参数获取帮助。")
        return 1
    if funcname is None:
        print("错误：未传入参数 \"funcname=\"。")
        print("请使用 --help 参数获取帮助。")
        return 1
    if functype is None:
        print("错误：未传入参数 \"functype=\"。")
        print("请使用 --help 参数获取帮助。")
        return 1

    try:
        os.mkdir(f"funcs/{dirname}")
    except FileExistsError:
        print(f"功能 \"{dirname}\" 已存在！")
        return 1

    try:
        open(f"funcs/{dirname}/about.json", "x", encoding="utf-8")
        with open(f"funcs/{dirname}/about.json", "r+", encoding="utf-8") as about_json:
            about_json.write(f"{{\"name\": \"{funcname}\", \"type\": \"{functype}\"}}\n")
        open(f"funcs/{dirname}/main.py", "x", encoding="utf-8")
        with open(f"funcs/{dirname}/main.py", "r+", encoding="utf-8") as main_py:
            main_py.write(f"from funcs.__main__.commands import *\ndef main():\n    print_title(\"{dirname}\")\n    print(\"This is a new {functype} named {funcname}.\")\n")
    except FileExistsError:
        print("错误：main.py 或 about.json 已存在！")
        return 1

    return 0

