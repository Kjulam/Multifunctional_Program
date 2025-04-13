def ugigyhhvsjjc(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            # 边界条件：第一列和最后一列均为1
            if j == 0 or j == i:
                row.append(1)
            else:
                # 中间的元素是上一行的两个相邻元素之和
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
