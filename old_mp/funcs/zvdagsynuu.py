NAME = "最大公因数"

from funcs.addons.commands import *
def run():
    print_title(NAME)
    a, b = map(int, input("输入两个数：").split())
    m = a; n = b
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    clear_screen()
    print_title(NAME)
    print(f"{a}和{b}的最大公因数是{n}")

