def run(a):
    return max(a) - min(a)


def read_line():
    a = list(map(int, input().split()))
    return a


def main():
    a = read_line()
    print(run(a))


if __name__ == '__main__':
    main()
