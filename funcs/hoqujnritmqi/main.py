import requests
from funcs.__main__.commands import *

def main():
    print_title("hoqujnritmqi")
    data_weather = requests.get(f"https://api.tangdouz.com/tq.php?dz={input("输入需要查询天气的地区：")}")
    print(f"\n{data_weather.text.replace(r"\r", "\n")}")
