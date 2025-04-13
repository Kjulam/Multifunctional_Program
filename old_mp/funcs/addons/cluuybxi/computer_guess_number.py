NAME = "猜数游戏"
from funcs.addons.commands import *

def computer_guess_number():
    print_title(NAME)
    print("欢迎来到计算机猜数字游戏！")
    print("请你在心里想一个1到100之间的整数，我会尝试猜出来。\n")
    pause()
    clear_screen()

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = (low + high) // 2  # 二分法猜测
        attempts += 1

        # 获取用户反馈
        print_title(NAME)
        feedback = input(f"我猜是 {guess}，对吗？\n"
                         "输入 h=太大 / l=太小 / c=正确：").lower().strip()
        clear_screen()

        # 处理反馈
        match feedback:
            case 'c':
                print_title(NAME)
                print(f"太棒了！你想的数是 {guess}。我只用了 {attempts} 次就猜中了！ヾ(≧▽≦*)o")
                break
            case 'h': high = guess - 1  # 调整上限
            case 'l': low = guess + 1  # 调整下限
            case _:
                print_title(NAME)
                print("无效输入！请输入 h/l/c\n")
                attempts -= 1  # 不计算无效回合
                pause()
                clear_screen()

        # 检测用户是否诚实
        if low > high:
            print_title(NAME)
            print("检测到矛盾！你肯定中途改数字了！(╬▔皿▔)╯")
            break

