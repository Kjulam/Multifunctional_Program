import os
from funcs.__main__.load_module_from_folder import *
# from funcs.__main__.create_new_function import *
from funcs.__main__.commands import *

def main(root_folder: str):
    functions_list = []
    modules_dict = {}
    
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        if os.path.isdir(folder_path):
            returned_value = load_module_from_folder(folder_path, functions_list, modules_dict)
            if returned_value == 1:
                return 1
    
    while True:
        # 打印功能列表
        folder_index = 1
        clear_screen()
        print_title("__main__")
        for func_name in functions_list:
            print(f"{folder_index}. {func_name}")
            folder_index += 1
        print("0. 退出程序")

        # 用户选择功能
        try:
            choice = int(input("\n请输入功能编号："))
            if choice == 0:
                clear_screen()
                print_title("__main__")
                return 0
            if 1 <= choice <= len(functions_list):
                selected_function = functions_list[choice - 1]
                if hasattr(modules_dict[selected_function], "main"):
                    clear_screen()
                    modules_dict[selected_function].main()
                else:
                    print(f"错误：{selected_function} 没有 main() 函数，无法运行。")
            else:
                print("无效的输入。请重新选择。")
        except ValueError:
            print("无效的输入。请重新选择。")
        except KeyboardInterrupt:
            clear_screen()
            print_title("__main__")
            return 1
        except Exception as e:
            print(f"发生错误：{e}")
        pause()



