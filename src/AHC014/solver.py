import random


random.seed(0)

def solve(n, m, x, y, lattice):
    k = 0
    ans = []
    cnt = 0
    use_line = set()


    # 利用済みの線分がないかをチェック
    def line_not_exists(x1, y1, x2, y2, x3, y3, x4, y4, use_line):
        ret = True
        if (x1, y1, x2, y2) in use_line:
            ret = False
        elif (x2, y2, x3, y3) in use_line:
            ret = False
        elif (x3, y3, x4, y4) in use_line:
            ret = False
        elif (x4, y4, x1, y1) in use_line:
            ret = False
        if ret:
            use_line.add((x1, y1, x2, y2))
            use_line.add((x2, y2, x1, y1))
            use_line.add((x2, y2, x3, y3))
            use_line.add((x3, y3, x2, y2))
            use_line.add((x3, y3, x4, y4))
            use_line.add((x4, y4, x3, y3))
            use_line.add((x4, y4, x1, y1))
            use_line.add((x1, y1, x4, y4))
        return ret, use_line


    # 2点間に格子点があるかチェック
    def is_point_not_exists(x1, y1, x2, y2):
        ret = True
        x_diff = x2 - x1
        y_diff = y2 - y1
        for i in range(1, max(abs(x_diff), abs(y_diff))):
            if x_diff == 0:
                x_gap = 0
            else:
                x_gap = x_diff / abs(x_diff)
            if y_diff == 0:
                y_gap = 0
            else:
                y_gap = y_diff / abs(y_diff)

            xi = x1 + i * x_gap
            yi = y1 + i * y_gap
            if (xi, yi) in lattice.keys():
                ret = False
                break
        return ret


    while cnt < 10000:
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
        if lattice[(x1, y1)] == -1 and is_point_not_exists(x1, y1, x4, y4) and is_point_not_exists(x1, y1, x2, y2):
            line_check, use_line = line_not_exists(x1, y1, x2, y2, x3, y3, x4, y4, use_line)
            if line_check:
                x.append(x1)
                y.append(y1)
                lattice[(x1, y1)] = len(x)-1
                ans.append([x1, y1, x2, y2, x3, y3, x4, y4])
                k += 1
                flag = True
                continue

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
            if not flag4_1 and not flag4_2:
                continue
            # x1の格子点をチェック
            x1 = x3
            y1 = y2 - (y3 - y2)
            if y1 >= 0:
                if lattice[(x1, y1)] == -1 and is_point_not_exists(x1, y1, x4, y4) and is_point_not_exists(x1, y1, x2, y2):
                    line_check, use_line = line_not_exists(x1, y1, x2, y2, x3, y3, x4, y4, use_line)
                    if line_check:
                        x.append(x1)
                        y.append(y1)
                        lattice[(x1, y1)] = len(x)-1
                        ans.append([x1, y1, x2, y2, x3, y3, x4, y4])
                        k += 1
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
