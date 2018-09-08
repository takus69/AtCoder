def run(n, k):
    a = 0
    b = 0
    for i in range(n):
        if (i+1) % k == 0:
            a += 1
        elif (i+1) % k == k/2:
            b += 1
    if k % 2 == 1:
        # return (n//k)**3
        return a**3
    else:
        # a = (n//k)**3
        # b = (((n - k/2)//k)+1)**3
        # return a + b
        return (a**3) + (b**3)


def read_line():
    n, k = map(int, input().split())
    return (n, k)


def main():
    n, k = read_line()
    print(run(n, k))


if __name__ == '__main__':
    main()
