def run(n, m, x, y, z):
    s = [x[i] + y[i] + z[i] for i in range(n)]
    s.sort(reverse=True)
    return sum(s[0:m])


def read_line():
    n, m = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        x[i], y[i], z[i] = map(int, input().split())
    return (n, m, x, y, z)


def main():
    n, m, x, y, z = read_line()
    print(run(n, m, x, y, z))


if __name__ == '__main__':
    main()
