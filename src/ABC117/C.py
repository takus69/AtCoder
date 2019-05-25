def run(N, M, X):
    if N >= M:
        return 0
    X = sorted(X)
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
    diff = sorted(diff)
    ret = X[-1] - X[0]
    for i in range(N-1):
        ret -= diff[-i-1]
    return ret


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    print(run(N, M, X))


if __name__ == '__main__':
    main()
