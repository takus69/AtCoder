import math


def run(n):
    ret = 0
    if n == 1:
        return n
    while True:
        ret += n % 10
        n = math.floor(n / 10)
        if n == 0:
            if ret == 1:
                return 10
            else:
                return ret


def read_line():
    n, = input().split()
    n = int(n)
    return n


def main():
    n = read_line()
    print(run(n))


if __name__ == '__main__':
    main()
