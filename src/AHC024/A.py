def parse_input():
    n, m = map(int, input().split())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    return n, m, c


def solver(n, m, c):
    pre_colors = '0'
    # 縦方向
    del_is = {}
    for i in range(n):
        if i in del_is.keys():
            continue
        colors = ''.join(map(str, c[i]))
        print(pre_colors, colors)
        if pre_colors == colors:
            del_is[i] = 1
        pre_colors = colors
    print(del_is.keys())
    
    # dを再構築
    d = [[0]*n for _ in range(n)]
    i2 = -1
    for i in range(n):
        if i in del_is.keys():
            continue
        else:
            i2 += 1
            for j in range(n):
                d[i2][j] = c[i][j]
    return d


if __name__ == '__main__':
    n, m, c = parse_input()
    d = solver(n, m, c)
    
    for i in range(n):
        print(' '.join(map(str, d[i])))
