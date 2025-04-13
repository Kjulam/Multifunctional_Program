NAME = "查询日期对应的星期数"

from funcs.addons.commands import *
from funcs.addons.uururiqiuuiuxyqi.is_leap import *

def run():
    print_title(NAME)
    year, month, day = map(int, input("输入一个日期：").split())
    clear_screen()
    print_title(NAME)
    a = year % 100
    y = (a // 4 + a) % 7
    if year < 2000: y += 1
    leap = is_leap(year)
    b = 426415305226 if leap == 0 else 426415305215
    c = 10 ** (month - 1)
    m = (b // c) % 10
    d = (y + m + day) % 7
    match d:
        case 0: print(f"{year} 年 {month} 月 {day} 日是星期日")
        case 1: print(f"{year} 年 {month} 月 {day} 日是星期一")
        case 2: print(f"{year} 年 {month} 月 {day} 日是星期二")
        case 3: print(f"{year} 年 {month} 月 {day} 日是星期三")
        case 4: print(f"{year} 年 {month} 月 {day} 日是星期四")
        case 5: print(f"{year} 年 {month} 月 {day} 日是星期五")
        case 6: print(f"{year} 年 {month} 月 {day} 日是星期六")


