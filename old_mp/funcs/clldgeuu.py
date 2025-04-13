NAME = "猜数（建议备一个计算器）"

from funcs.addons.commands import *
def run():
    print_title(NAME)
    print("请你随意想两个1~999的数字")
    pause()
    clear_screen()
    print_title(NAME)
    print("将你想的两个数相加，再乘1000，加上较大的数字，再减去较小的数字，等于多少？")
    m = int(input())
    a = m % 1000
    b = m // 1000
    c = max(a, b)
    d = min(a, b)
    x = (c + d) // 2
    y = (c - d) // 2
    clear_screen()
    print_title(NAME)
    print(f"你想的数是{x}和{y}")

