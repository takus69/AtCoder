def run(N, M, K, S, P):
    return (N, M, K, S, P)


def main():
    N, M = map(int, input().split())
    K = []
    S = []
    for _ in range(M):
        tmp = list(map(int, input().split()))
        K.append(tmp[0])
        S.append(tmp[1:])
    P = list(map(int, input().split()))
    print(run(N, M, K, S, P))


if __name__ == '__main__':
    main()
