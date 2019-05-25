def run(N, M, A, BC):
    # sort
    A.sort()
    # Aのカウント
    countA = {}
    for a in A:
        countA.setdefault(a, 0)
        countA[a] += 1
    # sort
    # 累積カウント
    sumA = {}
    sum = 0
    A = list(set(A))
    for a in A:
        sum += countA[a]
        sumA[a] = sum
    ret = 0
    C = list(BC.keys())
    C.sort(reverse=True)
    ai = 0
    now_N = N
    A.sort(reverse=True)
    first = True
    print('BC', BC)
    print('sumA', sumA)
    print('countA', countA)
    for c in C:
        print('c', c)
        # 最初c <= A[ai]はそのまま加算
        # c <= A[ai]は次のAへ
        if first:
            while c <= A[ai]:
                ret += A[ai]*countA[A[ai]]
                now_N -= countA[A[ai]]
                ai += 1
                print('first', ret)
                if ai >= len(A):
                    break
        print('now_N', now_N)
        print('ac', A[ai], c)
        if ai >= len(A):
            break
        while c <= A[ai]:
            ret += A[ai]*countA[A[ai]]
            now_N -= countA[A[ai]]
            ai += 1
            if ai >= len(A):
                break
        # c > A[ai]は置き換え
        b = BC[c]
        first = False
        print('a', A[ai])
        print('bc', b, c)
        if now_N >= b:
            ret += c*b
            now_N -= b
        else:
            ret += c*now_N
            now_N = 0
        print('now_N', now_N)
        print('ret', ret)
# 最後は残った分を足す
    print('now_N', now_N)
    A.sort()
    for a in A:
        if now_N > countA[a]:
            ret += a*countA[a]
            now_N -= countA[a]
        else:
            ret += a*now_N
            break
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
