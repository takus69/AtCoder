def run(n, a):
    max_a = max(a)
    min_a = min(a)
    return max_a - min_a


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
