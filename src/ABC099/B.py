def run(a, b):
    h1 = 0
    h2 = 0
    for i in range(1, 1000):
        h1 += i-1
        h2 += i
        if (h1 - a) == (h2 - b):
            return h1 - a


def main():
    a, b = map(int, input().split())
    print(run(a, b))


if __name__ == '__main__':
    main()
