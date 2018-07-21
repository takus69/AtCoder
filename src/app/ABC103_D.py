def run(n, m, ab):
    ab = sorted(ab)
    cnt = 1
    b = ab[0][1]
    c = b
    for i in range(1, m):
        a = ab[i][0]
        b = ab[i][1]
        if a < c and c <= b:
            pass
        elif c <= a:
            cnt += 1
            c = b
        else:
            c = b
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
