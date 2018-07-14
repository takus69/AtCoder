def run(n, s):
    print(n, s)


def read_line():
    n = int(input())
    s = input()
    return (n, s)


def main():
    n, s = read_line()
    print(run(n, s))


if __name__ == '__main__':
    main()
