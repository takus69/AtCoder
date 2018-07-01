def run(n, a):
    sum_a = [sum(a[0:i+1]) for i in range(n)]
    ret = sum_a[n - 1]
    for i in range(2, n-1):
        j_l = search_j(sum_a[: i], 0)
        j_r = search_j(sum_a[i:], sum_a[i - 1]) + i
        p = sum_a[j_l]
        q = sum_a[i - 1] - p
        r = sum_a[j_r] - q - p
        s = sum_a[n - 1] - r - q - p
        diff = max(p, q, r, s) - min(p, q, r, s)
        if ret > diff:
            ret = diff
    return ret


def search_j(sum_a, before):
    n = len(sum_a)
    sum_l = sum_a[0] - before
    sum_r = sum_a[n - 1] - sum_a[0]
    diff1 = sum_r - sum_l
    ret = 0
    for i in range(n - 1):
        sum_l = sum_a[i] - before
        sum_r = sum_a[n - 1] - sum_a[i]
        diff2 = sum_r - sum_l
        if diff2 < 0:
            if abs(diff1) < abs(diff2):
                return i - 1
            else:
                return i
        else:
            diff1 = diff2
            ret = i
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
