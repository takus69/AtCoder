def run(n, a):
    a = [a[i]-i-1 for i in range(len(a))]
    a.sort()
    m = a[int((n-1)/2)]
    ret = 0
    for ai in a:
        ret += abs(ai - m)
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
