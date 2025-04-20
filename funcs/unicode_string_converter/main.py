from funcs.__main__.commands import *
from funcs.unicode_string_converter.string_to_unicode import string_to_unicode

def main():
    print_title("unicode_string_converter")
    string_text = input("输入一段内容：")
    unicode_text = string_to_unicode(string_text)
    print(unicode_text)

