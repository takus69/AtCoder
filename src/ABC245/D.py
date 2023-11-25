N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [-1] * (M+1)
for i in range(M+1):
    # print('A:', A)
    # print('B:', B)
    # print('C:', C)
    tmp_C = C[N+M-i]
    for j in range(i):
        if N-i+j < 0:
            continue
        # print('j, i, tmp_C, A[N-j], B[M-i+j]', j, i, tmp_C, A[N-i+j], B[M-j])
        tmp_C -= A[N-i+j]*B[M-j]
    # print('i, tmp_C, A[N]', i, tmp_C, A[N])
    B[-i-1] = tmp_C // A[N]

print(' '.join(map(str, B)))
