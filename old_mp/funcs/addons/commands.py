import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("请按回车键继续...")

def print_title(program_title):
    print("="*5, program_title, "="*5, "\n")

