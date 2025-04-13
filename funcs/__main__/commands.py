import os, json

def print_title(function_dir_name):
    output_decorate = "=" * 5
    try:
        print(f"{output_decorate} {json.load(open(f"funcs/{function_dir_name}/about.json", "r", encoding="utf-8"))["name"]} {output_decorate}\n")
    except FileNotFoundError:
        print(f"请检查目录 \"./funcs/{function_dir_name}/\" 是否存在！")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("请按回车键继续...")


