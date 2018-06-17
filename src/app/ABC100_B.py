def run(d, n):
    if n == 100:
        return (n + 1) * (100 ** d)
    else:
        return n * (100 ** d)


def read_line():
    a, b = input().split()
    a = int(a)
    b = int(b)
    return (a, b)


def main():
    d, n = read_line()
    print(run(d, n))


if __name__ == '__main__':
    main()
