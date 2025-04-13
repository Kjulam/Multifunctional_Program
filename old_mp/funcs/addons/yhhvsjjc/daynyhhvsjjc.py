def daynyhhvsjjc(triangle):
    # 找到最长的行的长度，用于对齐
    max_length = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        # 将每一行的元素转换为字符串并居中对齐
        print(' '.join(map(str, row)).center(max_length))
