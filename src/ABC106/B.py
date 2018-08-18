def run(n):
    if n < 105:
        return 0
    elif n < 135:
        return 1
    elif n < 165:
        return 2
    elif n < 189:
        return 3
    elif n < 195:
        return 4
    else:
        return 5


def read_line():
    n = int(input())
    return n


def main():
    n = read_line()
    print(run(n))


if __name__ == '__main__':
    main()
