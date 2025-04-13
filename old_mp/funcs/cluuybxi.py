NAME = "猜数游戏"

from funcs.addons.commands import *
from funcs.addons.cluuybxi.user_guess_number import *
from funcs.addons.cluuybxi.computer_guess_number import *

def run():
    while True:
        print_title(NAME)
        print("欢迎来到猜数游戏！这里有两种模式供你选择：\n1.计算机生成数字，你来猜；\n2.你想一个数字，计算机来猜；\n0.退出。\n")
        match input("请做出选择："):
            case "1":
                clear_screen()
                user_guess_number()
                pause()
                clear_screen()
            case "2":
                clear_screen()
                computer_guess_number()
                pause()
                clear_screen()
            case "0": return
            case _:
                print("你这输入不对啊，重来！")
                pause()
                clear_screen()


