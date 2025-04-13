NAME = "读心术猜数"

from funcs.addons.commands import *
def run():
    print_title(NAME)
    t = [""] * 6
    t[0] = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31"
    t[1] = "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31"
    t[2] = "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31"
    t[3] = "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31"
    t[4] = "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31"
    t[5] = "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31"
    
    print("请你从下面一堆数中选一个并记在心里。")
    print(t[0])
    pause()
    clear_screen()
    
    a = [0] * 6
    for i in range(1, 6):
        while True:
            print_title(NAME)
            print(f"问题{i}：下面的数中有你想的吗？0：没有 1：有")
            print(t[i])
            try:
                a[i] = int(input("请输入（0没有 / 1有）: "))
                clear_screen()
                if a[i] in (0, 1):
                    break
                else:
                    print("输入错误，请重新输入！")
                    pause()
                    clear_screen()
            except ValueError:
                print("请输入数字0或1！")
                pause()
                clear_screen()
        clear_screen()
    
    ans = 1 * a[5] + 2 * a[4] + 4 * a[3] + 8 * a[2] + 16 * a[1]
    print_title(NAME)
    print(f"你想的数是 {ans}")

