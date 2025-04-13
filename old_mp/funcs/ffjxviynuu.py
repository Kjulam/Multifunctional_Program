NAME = "分解质因数"

from funcs.addons.commands import *
def run():
    i = 2
    print_title(NAME)
    a = int(input("输入一个数："))
    clear_screen()
    print_title(NAME)
    print(f"{a} = ", end="")
    while True:
        if i * i > a:
            if a > 1:
                print(a, end="")
                break
            else: break
        else:
            if a % i == 0:
                print(f"{i} * ", end="")
                a //= i
            else: i += 1
    print()

