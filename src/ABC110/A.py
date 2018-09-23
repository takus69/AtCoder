def run(a, b, c):
    s = sorted([a, b, c])
    return 10*s[2]+s[1]+s[0]


def main():
    a, b, c = map(int, input().split())
    print(run(a, b, c))


if __name__ == '__main__':
    main()
