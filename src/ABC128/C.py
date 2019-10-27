def run(N, M, K, S, P):
    ret = 0
    for i in range(2 ** N):
        bit = bin(i)[2:].zfill(N)
        chk = True
        for j in range(M):
            cnt = 0
            for s in S[j]:
                cnt += int(bit[s-1])
            if cnt % 2 == P[j]:
                pass
            else:
                chk = False
                break
        if chk:
            ret += 1
    return ret


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
