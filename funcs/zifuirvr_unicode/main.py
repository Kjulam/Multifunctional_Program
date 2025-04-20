from funcs.__main__.commands import *
from funcs.zifuirvr_unicode.string_to_unicode import string_to_unicode

def main():
    print_title("zifuirvr_unicode")
    string_text = input("输入一段内容：")
    unicode_text = string_to_unicode(string_text)
    print(unicode_text)

