def run(n, x, a):
    a = sorted(a)
    cnt = 0
    for i in range(n):
        x -= a[i]
        if x >= 0:
            cnt += 1
    if x > 0:
        cnt -= 1
    return cnt


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(run(n, x, a))


if __name__ == '__main__':
    main()
