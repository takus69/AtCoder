import fractions


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
        g = fractions.gcd(b, d)
        amodb = a % b
        if g == 1:
            if b - 1 > c:
                return 'No'
        elif g == b:
            if amodb > c:
                return 'No'
        else:
            if (b - g) > c:
                return 'No'
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
