import fractions


def run(n, x, xx):
    xx.append(x)
    xx = sorted(xx)
    d = [xx[i+1]-xx[i] for i in range(n)]
    d = sorted(d)
    min_d = d[0]
    if len(d) == 1:
        pass
    else:
        for i in range(1, len(d)):
            min_d = fractions.gcd(min_d, d[i])
    return min_d


def main():
    n, x = map(int, input().split())
    xx = list(map(int, input().split()))
    print(run(n, x, xx))


if __name__ == '__main__':
    main()
