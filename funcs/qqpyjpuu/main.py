from funcs.__main__.commands import *
def main():
    print_title("qqpyjpuu")
    a = list(map(int, input("输入各个数字：").split()))
    temp = 0
    for i in range(len(a)):
        temp += a[i]
    print(f"平均数：{(temp / len(a)): g}")
