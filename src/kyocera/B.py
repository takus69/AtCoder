def run(N, K):
    for _ in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = N * 1000 + 200
    return N


def main():
    N, K = map(int, input().split())
    print(run(N, K))


if __name__ == '__main__':
    main()
