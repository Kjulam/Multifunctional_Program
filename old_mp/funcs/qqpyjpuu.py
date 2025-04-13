NAME = "求平均数"

from funcs.addons.commands import *
def run():
    print_title(NAME)
    a = list(map(int, input("请输入各个数字：").split()))
    temp = 0
    for i in range(len(a)):
        temp += a[i]
    print("平均数：%g"%(temp / len(a)))

