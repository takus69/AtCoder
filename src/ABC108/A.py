def run(k):
    return (k // 2)*(k // 2 + k % 2)


def read_line():
    k = int(input())
    return k


def main():
    k = read_line()
    print(run(k))


if __name__ == '__main__':
    main()
