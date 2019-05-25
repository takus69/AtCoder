def run(N, M, A, BC):
    # sort
    A.sort()
    # Aのカウント
    countA = {}
    for a in A:
        countA.setdefault(a, 0)
        countA[a] += 1
    # sort
    A = list(set(A))
    C = list(BC.keys())
    C.sort(reverse=True)
    A.sort(reverse=True)
    ai = 0
    ci = 0
    a = A[ai]
    c = C[ci]
    now_N = N
    ret = 0
    while now_N > 0:
        # Aが大きい場合はai+1しながら加算
        while c <= a:
            cnt = countA[a]
            if now_N > cnt:
                ret += a*cnt
                now_N -= cnt
                ai += 1
            else:
                ret += a*now_N
                now_N = 0
                break
            if ai < len(A):
                a = A[ai]
            else:
                a = 0
        # Cが大きい場合は加算して次のCへ
        while c >= a:
            b = BC[c]
            if now_N > b:
                ret += c*b
                now_N -= b
                ci += 1
            else:
                ret += c*now_N
                now_N = 0
                break
            if ci < len(C):
                c = C[ci]
            else:
                c = 0
    return ret


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = {}
    for _ in range(M):
        B, C = list(map(int, input().split()))
        BC.setdefault(C, 0)
        BC[C] += B
    print(run(N, M, A, BC))


if __name__ == '__main__':
    main()
