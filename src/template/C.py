def run(n, a):
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
    return cnt


def read_line():
    n, = input().split()
    a = input().split()
    n = int(n)
    a = [int(a[i]) for i in range(n)]
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
