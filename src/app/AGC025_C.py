def run(n, ln, rn):
    dic = {}
    for i in range(n):
        dic[i] = [ln[i], rn[i]]
    sort_ln = sorted(dic.items(), key=lambda x: -x[1][0])
    sort_rn = sorted(dic.items(), key=lambda x: x[1][1])
    if abs(max([l[1][0] for l in sort_ln])) > abs(min([r[1][1] for r in sort_rn])):
        idx = 0
    else:
        idx = 1
    ret = 0
    now = 0
    for i in range(n):
        if idx == 0:
            if sort_ln[0][1][0] < 0:
                if 0 < sort_ln[0][1][1]:
                    return ret + abs(now)
            if sort_ln[0][1][0] == 0:
                return ret + abs(now)
            if sort_ln[0][1][1] == 0:
                return ret + abs(now)
            move = sort_ln[0][1][idx]
            ret += abs(move - now)
            now = move
            idx = 1
            di = sort_ln[0][0]
        else:
            if sort_rn[0][1][0] < 0:
                if 0 < sort_rn[0][1][1]:
                    return ret + abs(now)
            if sort_rn[0][1][0] == 0:
                return ret + abs(now)
            if sort_rn[0][1][1] == 0:
                return ret + abs(now)
            move = sort_rn[0][1][idx]
            ret += abs(move - now)
            now = move
            idx = 0
            di = sort_rn[0][0]
        del dic[di]
        sort_ln = sorted(dic.items(), key=lambda x: -x[1][0])
        sort_rn = sorted(dic.items(), key=lambda x: x[1][1])
    ret += abs(now)
    return ret


def read_line():
    n = int(input())
    ln = []
    rn = []
    for i in range(n):
        l, r = list(map(int, input().split()))
        ln.append(l)
        rn.append(r)
    return (n, ln, rn)


def main():
    n, ln, rn = read_line()
    print(run(n, ln, rn))


if __name__ == '__main__':
    main()
