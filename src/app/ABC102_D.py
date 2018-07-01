def run(n, a):
    sp = [n-3, n-2, n-1]
    (p, q, r, s) = calc_sum(a, sp)
    max1 = max((p, q, r, s))
    min1 = min((p, q, r, s))
    diff1 = max1 - min1
    diff_t = 0
    t_sp = target_sp(sp, n)
    print(t_sp)
    if t_sp == []:
        return diff1
    while(diff1 != diff_t):
        diff_t = diff1
        for t in t_sp:
            sp_c = sp.copy()
            sp_c[t] -= 1
            (p, q, r, s) = calc_sum(a, sp_c)
            max2 = max((p, q, r, s))
            min2 = min((p, q, r, s))
            diff2 = max2 - min2
            if diff1 > diff2:
                diff1 = diff2
                sp = sp_c.copy()
                t_sp = target_sp(sp, n)
                break
    print(a)
    print(sp)
    print(t_sp)
    return diff1


def calc_sum(a, sp):
    p = sum(a[:sp[0]])
    q = sum(a[sp[0]:sp[1]])
    r = sum(a[sp[1]:sp[2]])
    s = sum(a[sp[2]:])
    return (p, q, r, s)


def target_sp(sp, n):
    ret = []
    if sp[0] > 1:
        ret.append(0)
    if sp[1] - sp[0] > 1:
        ret.append(1)
    if sp[2] - sp[1] > 1:
        ret.append(2)
    return ret


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
