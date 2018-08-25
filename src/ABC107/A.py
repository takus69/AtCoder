def run(a, b):
    return a - b + 1


def read_line():
    a, b = input().split()
    a = int(a)
    b = int(b)
    return (a, b)


def main():
    a, b = read_line()
    print(run(a, b))


if __name__ == '__main__':
    main()
