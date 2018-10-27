def run(N, A):
    A = sorted(A)
    ret = 0
    for i in range(N//2):
        ret += A[-(i+1)] - A[i]
        aa = A[-(i+1)] - A[i]
        if N - (i+1) != i + 1:
            ret += A[-(i+1)] - A[i+1]
            aa = A[-(i+1)] - A[i+1]
    i = N//2 - 1
    ret -= aa
    ret += A[i+1] - A[0]

    ret2 = 0
    for i in range(N//2):
        ret2 += A[-(i+1)] - A[i]
        aa = A[-(i+1)] - A[i]
        if N - (i+2) != i:
            ret2 += A[-(i+2)] - A[i]
            aa = A[-(i+2)] - A[i]
    i = N//2 - 1
    ret2 -= aa
    ret2 += A[-1] - A[-(i+2)]
    return max(ret, ret2)


def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    print(run(N, A))


if __name__ == '__main__':
    main()
