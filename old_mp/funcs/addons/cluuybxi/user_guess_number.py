NAME = "猜数游戏"

import random
from funcs.addons.commands import *

def user_guess_number():
    # 生成一个1到100之间的随机数
    target_number = random.randint(1, 100)
    attempts = 0

    print_title(NAME)
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。")

    while True:
        try:
            # 获取用户的猜测
            user_guess = int(input("\n请输入你的猜测（1-100）："))
            attempts += 1

            # 检查用户的猜测
            if user_guess < target_number:
                print("太小了！再试一次。")
            elif user_guess > target_number:
                print("太大了！再试一次。")
            else:
                print(f"恭喜你！你猜对了！答案是 {target_number}。")
                print(f"你总共尝试了 {attempts} 次。")
                break
        except ValueError:
            print("无效输入！请输入一个有效的数字。")

