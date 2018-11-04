def run(a, b):
    return int(a + b/2)


def main():
    a, b, = map(int, input().split())
    print(run(a, b))


if __name__ == '__main__':
    main()
