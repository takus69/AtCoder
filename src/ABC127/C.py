def run(N, M, L, R):
    maxL = max(L)
    minR = min(R)
    if maxL > minR:
        ret = 0
    else:
        ret = minR - maxL + 1
    return ret


def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        LR = list(map(int, input().split()))
        L.append(LR[0])
        R.append(LR[1])
    print(run(N, M, L, R))


if __name__ == '__main__':
    main()
