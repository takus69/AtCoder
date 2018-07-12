def run(n, a, b, k):
    print(n, a, b, k)


def read_line():
    n, a, b, k = list(map(int, input().split()))
    return (n, a, b, k)


def main():
    n, a, b, k = read_line()
    print(run(n, a, b, k))


if __name__ == '__main__':
    main()
