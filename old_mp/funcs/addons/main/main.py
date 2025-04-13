NAME = "多功能程序"

from funcs.addons.commands import *
from funcs.addons.main.load_modules import *
import sys

def run():
    modules = load_modules()

    while True:
        clear_screen()
        print_title(NAME)
        print("可用功能：")
        for i, (name, _) in enumerate(modules.items(), 1):
            print(f"{i}. {name}")
        print("0. 退出程序")

        try:
            choice = input("\n请输入功能编号：")
            clear_screen()
            if choice == "0":
                break

            index = int(choice) - 1
            selected = list(modules.values())[index]
            selected()  # 执行对应功能

        except (ValueError, IndexError):
            clear_screen()
            print_title(NAME)
            print("无效的输入，请重新选择")
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            clear_screen()
            print_title(NAME)
            print(f"发生错误: {str(e)}")
        pause()

