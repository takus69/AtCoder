def run(N, K, t, d):
    return (N, K, t, d)


def main():
    N, K = map(int, input().split())
    t = []
    d = []
    for i in range(N):
        ti, di = map(int, input().split())
        t.append(ti)
        d.append(di)
    print(run(N, K, t, d))


if __name__ == '__main__':
    main()
