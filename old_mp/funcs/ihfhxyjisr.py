NAME = "长方形计算"

from funcs.addons.commands import *
def run():
    print_title(NAME)
    a, b = map(int, input("请输入长方形的长和宽：").split())
    c = (a + b) *2
    s = a * b
    print(f"周长：{c}；面积：{s}")

