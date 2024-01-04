T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = 'no'
i, j = 0, 0
while True:
    if i <= N and j == M:
        ans = 'yes'
        break
    elif i == N and j < M:
        ans = 'no'
        break
    a = A[i]
    b = B[j]
    # print('i, j, a, b, T:', i, j, a, b, T)
    if a <= b <= a+T:
        j += 1
    i += 1

print(ans)
