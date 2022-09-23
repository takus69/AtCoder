import random


random.seed(0)

def solve(n, m, x, y, lattice):
    k = 0
    ans = []
    cnt = 0

    while cnt < 1000:
        cnt += 1
        t_i = random.randint(0, m-1)
        x2 = x[t_i]
        y2 = y[t_i]
        ## 軸と並行
        flag = False
        # y軸下方向の探索
        flag3 = False
        for yy in range(y2+1, n):
            if lattice[(x2, yy)] >= 0:
                y3 = yy
                x3 = x2
                flag3 = True
                break
        if not flag3:
            for yy in range(y2-1, -1, -1):
                if lattice[(x2, yy)] >= 0:
                    y3 = yy
                    x3 = x2
                    flag3 = True
                    break
        if not flag3:
            break
        # x軸右方向の探索
        flag4 = False
        for xx in range(x2+1, n):
            if lattice[(xx, y3)] >= 0:
                x4 = xx
                y4 = y3
                flag4 = True
                break
        # x軸左方向の探索
        if not flag4:
            for xx in range(x2-1, -1, -1):
                if lattice[(xx, y3)] >= 0:
                    x4 = xx
                    y4 = y3
                    flag4 = True
                    break
        if not flag4:
            break
        # x1の格子点をチェック
        x1 = x4
        y1 = y2
        if lattice[(x1, y1)] == -1:
            x.append(x1)
            y.append(y1)
            lattice[(x1, y1)] = len(x)-1
            ans.append([x1, y1, x2, y2, x3, y3, x4, y4])
            k += 1
            flag = True
            continue

    '''
        ## 45度
        if not flag:
            # y軸下方向の探索
            flag3_1 = False
            flag3_2 = False
            for i in range(n-y2-1):
                if x2+i+1 <= n-1:
                    if lattice[(x2+i+1, y2+i+1)] >= 0:
                        x3 = x2+i+1
                        y3 = y2+i+1
                        flag3_1 = True
                        break
                if x2-i-1 >= 0:
                    if lattice[(x2-i-1, y2+i+1)] >= 0:
                        x3 = x2-i-1
                        y3 = y2+i+1
                        flag3_2 = True
                        break
            # x軸右方向の探索
            flag4_1 = False
            flag4_2 = False
            if flag3_1:
                for i in range(n-x3-1):
                    if y3-i-1 >= 0:
                        if lattice[(x3+i+1, y3-i-1)] >= 0:
                            x4 = x3+i+1
                            y4 = y3-i-1
                            flag4_1 = True
                            break
            elif flag3_2:
                for i in range(x3-1):
                    if y3-i-1 >= 0:
                        if lattice[(x3-i-1, y3-i-1)] >= 0:
                            x4 = x3-i-1
                            y4 = y3-i-1
                            flag4_2 = True
                            break
            else:
                break
            if not flag4_1 and not flag4_2:
                break
            # x1の格子点をチェック
            x1 = x3
            y1 = y2 - (y3 - y2)
            if y1 >= 0:
                if lattice[(x1, y1)] == -1:
                    x.append(x1)
                    y.append(y1)
                    lattice[(x1, y1)] = len(x)-1
                    ans.append([x1, y1, x2, y2, x3, y3, x4, y4])
                    k += 1
    '''
    return k, ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    lattice = {}
    for x in range(n):
        for y in range(n):
            lattice[(x, y)] = -1
    x, y = [], []
    for i in range(m):
        xx, yy = map(int, input().split())
        x.append(xx)
        y.append(yy)
        lattice[(xx, yy)] = i

    k, ans = solve(n, m, x, y, lattice)
    print(k)
    for i in range(k):
        print(' '.join(map(str, ans[i])))
