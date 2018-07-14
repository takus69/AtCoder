def run(n, a):
    now = a[0]
    cnt = 0
    if n == 1:
        return 0
    i = 1
    while(True):
        if now == a[i]:
            cnt += 1
            i += 1
            if i >= n:
                return cnt
            now = a[i]
            i += 1
            if i >= n:
                return cnt
        else:
            now = a[i]
            i += 1
            if i >= n:
                return cnt


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
