def run(a):
    return a[0] * a[1] // 2


def main():
    a = list(map(int, input().split()))
    print(run(a))


if __name__ == '__main__':
    main()
