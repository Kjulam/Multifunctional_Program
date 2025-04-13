from funcs.__main__.commands import *

def main():
    i = 2
    print_title("ffjxviynuu")
    a = int(input("输入一个数："))
    clear_screen()
    print_title("ffjxviynuu")
    print(f"{a} = ", end="")
    while True:
        if i * i > a:
            if a > 1:
                print(f"{a}", end="")
                break
            else:
                break
        else:
            if a % i == 0:
                print(f"{i} * ", end="")
                a //= i
            else:
                i += 1
    print()

