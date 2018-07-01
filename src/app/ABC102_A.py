def run(n):
    if n % 2 == 0:
        return n
    else:
        return n * 2


def read_line():
    n = int(input())
    return n


def main():
    n = read_line()
    print(run(n))


if __name__ == '__main__':
    main()
