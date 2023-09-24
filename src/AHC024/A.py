import random


def parse_input():
    n, m = map(int, input().split())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    return n, m, c


def solver(n, m, c):
    # dにcをコピー
    d = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j] = c[i][j]

    # 連結を確認
    con = parse_graph(n, m, c)

    # 乱択
    del_is = {}
    for _ in range(100):
        # 行か列か、どの位置かを乱数で取得
        # r_or_c = random.randint(0, 1)
        r_or_c = 0
        i = random.randint(0, n-1)
        # 削除
        tmp_d = del_row_or_col(r_or_c, i, d, n)
        tmp_keys = set(del_is.keys())
        tmp_keys.add(i)
        tmp_d2 = reconstruct(tmp_d, tmp_keys)
        # 連結が崩れていなければ採用
        if check(n, m, tmp_d2, con):
            d = tmp_d
            del_is[i] = 1
    
    # dを再構築(上記は論理)
    d = reconstruct(d, del_is.keys())

    return d


def parse_graph(n, m, d):
    # 0の連結も含む
    con = {i: [] for i in range(m+1)}

    # 0の連結構築
    con0 = d[0] + d[:][0] + d[:][-1] + d[-1] + [0]
    con[0] = con0
    for i in set(con0):
        con[i].append(0)

    # 中の連結構築
    ## 横方向
    for i in range(n):
        pre = 0
        for j in range(n):
            v = d[i][j]
            if v == pre:
                continue
            else:
                con[pre].append(v)
                con[v].append(pre)
            pre = v
    ## 縦方向
    for j in range(n):
        pre = 0
        for i in range(n):
            v = d[i][j]
            if v == pre:
                continue
            else:
                con[pre].append(v)
                con[v].append(pre)
            pre = v
    
    # 連結要素の重複削除
    for k in con.keys():
        con[k] = set(con[k])
    return con


def check(n, m, d, con):
    con2 = parse_graph(n, m, d)
    if con2 == con:
        return True
    else:
        return False


def reconstruct(d, del_keys):
    # dを再構築
    n = len(d)
    d2 = [[0]*n for _ in range(n)]
    i2 = -1
    for i in range(n):
        if i in del_keys:
            continue
        else:
            i2 += 1
            for j in range(n):
                d2[i2][j] = d[i][j]
    return d2
    

def del_row_or_col(r_or_c, i2, d, n):
    # r_or_cは、0が行、1が列
    d2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d2[i][j] = d[i][j]
    if r_or_c == 0:
        for j in range(n):
            d2[i2][j] = 0
    else:
        for j in range(n):
            d2[j][i2] = 0
    return d2


if __name__ == '__main__':
    n, m, c = parse_input()
    d = solver(n, m, c)
    
    for i in range(n):
        print(' '.join(map(str, d[i])))
