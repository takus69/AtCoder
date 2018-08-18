def run(n, m, qq, l, r, p, q):
    cnt = []
    # lでソート済みと仮定
    # lr = []
    # for i in range(m):
    #     lr.append([l[i], r[i]])
    # print(lr)
    # sort_l = sorted(lr, key=lambda x: -x[1][0])
    # print(sort_l)
    dic = {}
    for i in range(qq):
        tmp_cnt = 0
        if (p[i], q[i]) in dic:
            cnt.append(dic[(p[i], q[i])])
        else:
            for j in range(m):
                if p[i] <= l[j] and r[j] <= q[i]:
                    tmp_cnt += 1
            cnt.append(tmp_cnt)
            dic[(p[i], q[i])] = tmp_cnt
    return cnt


def read_line():
    n, m, qq = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        tl, tr = map(int, input().split())
        l.append(tl)
        r.append(tr)
    p = []
    q = []
    for i in range(qq):
        tp, tq = map(int, input().split())
        p.append(tp)
        q.append(tq)
    return (n, m, qq, l, r, p, q)


def main():
    n, m, qq, l, r, p, q = read_line()
    ret = run(n, m, qq, l, r, p, q)
    for i in range(len(ret)):
        print(ret[i])


if __name__ == '__main__':
    main()
