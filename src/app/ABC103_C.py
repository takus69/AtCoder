def run(n, a):
    '''
    g = a[0]
    for j in range(1, len(a)):
        g = int(g * a[j] / fractions.gcd(g, a[j]))
    m = g
    tmp_f = 0
    f = 0
    for i in range(1, m+1):
        tmp_f = 0
        for j in range(len(a)):
            tmp_f += i % a[j]
        f = max(f, tmp_f)
    '''
    f = 0
    for i in range(len(a)):
        f += a[i] - 1
    return f


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
