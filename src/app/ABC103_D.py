def run(n, m, ab):
    ab = sorted(ab)
    cnt = 1
    b = ab[0][1]
    for i in range(1, m):
        a = ab[i][0]
        if b < a:
            cnt += 1
        b = ab[i][1]
    return cnt


def read_line():
    n, m = list(map(int, input().split()))
    ab = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        ab.append([a, b])
    return (n, m, ab)


def main():
    n, m, ab = read_line()
    print(run(n, m, ab))


if __name__ == '__main__':
    main()
