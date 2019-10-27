def run(N, K, AN, FN):
    AN = sorted(AN, reverse=True)
    FN = sorted(FN)
    for i in range(N):
        if K == 0:
            break
        elif AN[i] <= K:
            K -= AN[i]
            AN[i] = 0
        else:
            AN[i] -= K
            K = 0
    AN = sorted(AN, reverse=True)
    FN = sorted(FN)
    ret = []
    for i in range(N):
        ret.append(AN[i] * FN[i])
    return max(ret)


def main():
    N, K = map(int, input().split())
    AN = list(map(int, input().split()))
    FN = list(map(int, input().split()))
    print(run(N, K, AN, FN))


if __name__ == '__main__':
    main()
