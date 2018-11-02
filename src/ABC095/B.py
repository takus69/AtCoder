def run(N, X, M):
    cnt = len(M)
    X -= sum(M)
    min_m = min(M)
    cnt += (X // min_m)
    return cnt


def main():
    N, X = map(int, input().split())
    M = []
    for i in range(N):
        M.append(int(input()))
    print(run(N, X, M))


if __name__ == '__main__':
    main()
