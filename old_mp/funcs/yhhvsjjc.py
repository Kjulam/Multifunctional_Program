NAME = "杨辉三角生成器"
from funcs.addons.yhhvsjjc.ugigyhhvsjjc import *
from funcs.addons.yhhvsjjc.daynyhhvsjjc import *
from funcs.addons.commands import *
def run():
    print_title(NAME)
    n = int(input("请输入杨辉三角的行数："))
    pascals_triangle = ugigyhhvsjjc(n)
    daynyhhvsjjc(pascals_triangle)

