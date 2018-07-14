def run(t, a, b, c, d):
    ret = []
    for i in range(t):
        ret.append(check(a[i], b[i], c[i], d[i]))
    return ret


def check(a, b, c, d):
    if a < b:
        return 'No'
    if d < b:
        return 'No'
    if c < b:
        if a % b > c:
            return 'No'
        if d % b == 0:
            return 'Yes'
        if b % 2 == 0 and d % 2 == 0:
            if (d - b) % (b - c) == 0:
                return 'Yes'
            else:
                return 'No'
        else:
            if b - c > 1:
                return 'No'
#        if b % 2 == 1 or a % 2 == 1 or d % 2 == 1:
#            if b - c > 1:
#                return 'No'
#        else:
#            if (d - b) % (b - c) == 0:
#                return 'Yes'
#            else:
#                return 'No'
    return 'Yes'


def read_line():
    t = int(input())
    a = []
    b = []
    c = []
    d = []
    for i in range(t):
        at, bt, ct, dt = list(map(int, input().split()))
        a.append(at)
        b.append(bt)
        c.append(ct)
        d.append(dt)
    return (t, a, b, c, d)


def main():
    t, a, b, c, d = read_line()
    ret = run(t, a, b, c, d)
    for i in range(t):
        print(ret[i])


if __name__ == '__main__':
    main()
