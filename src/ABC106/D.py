def run(n, m, qq, l, r, p, q):
    cnt = {}
    sum = {}
    ret = []
    for i in range(n+1):
        for j in range(n+1):
            cnt[i, j] = 0
            sum[i, j] = 0
    for i in range(m):
        cnt[(l[i], r[i])] += 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum[i, j] = cnt[i, j] + sum[i-1, j] + sum[i, j-1] - sum[i-1, j-1]
    for i in range(qq):
        ret.append(sum[q[i], q[i]] - sum[p[i]-1, q[i]] - sum[q[i],
                   p[i]-1] + sum[p[i]-1, p[i]-1])
    return ret


def read_line():
    n, m, qq = map(int, input().split())
    ll = []
    r = []
    for il in range(m):
        tl, tr = map(int, input().split())
        ll.append(tl)
        r.append(tr)
    p = []
    q = []
    for i in range(qq):
        tp, tq = map(int, input().split())
        p.append(tp)
        q.append(tq)
    return (n, m, qq, ll, r, p, q)


def main():
    n, m, qq, l, r, p, q = read_line()
    ret = run(n, m, qq, l, r, p, q)
    for i in range(len(ret)):
        print(ret[i])


if __name__ == '__main__':
    main()
