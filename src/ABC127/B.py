def run(r, D, x2000):
    x = x2000
    for i in range(10):
        x = r*x - D
        print(x)


def main():
    r, D, x2000 = map(int, input().split())
    run(r, D, x2000)


if __name__ == '__main__':
    main()
