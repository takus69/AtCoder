def run(N, Q, A, XY):
    return rec_count(A, XY, 0)


def rec_count(A, XY, i):
    div = 10**9 + 7
    if i >= len(XY):
        return count_swap(A) % div
    A_swap = swap(A, XY[i])
    return (rec_count(A, XY, i+1) + rec_count(A_swap, XY, i+1)) % div


def swap(A, XY):
    A_swap = A.copy()
    X = XY[0] - 1
    Y = XY[1] - 1
    A_swap[X], A_swap[Y] = A[Y], A[X]
    return A_swap


def count_swap(A):
    cnt = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                cnt += 1
    return cnt


def main():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))
    XY = []
    for _ in range(Q):
        XY.append(list(map(int, input().split())))
    print(run(N, Q, A, XY))


if __name__ == '__main__':
    main()
