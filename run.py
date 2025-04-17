# Multifunctional_Program
import sys
from funcs.__main__.main import main

def run():
    if len(sys.argv) >= 2:
        from funcs.__main__.print_help import print_help
        if "--help" in sys.argv:
            print_help()

        elif "--create-new-module" in sys.argv:
            from funcs.__main__.create_new_module import create_new_module
            create_new_module(sys.argv)

        else:
            print("错误：你不会加参数就别加了。")
            print_help()
            sys.exit(1)

        sys.exit(0)

    print(f"程序已退出，退出代码：{main("funcs")}。")

if __name__ == "__main__":
    run()

