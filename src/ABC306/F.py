N, M = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A2 = {}
for i in range(N):
    for j in range(i+1, N):
        a2 = A[i] + A[j]
        a2.sort()
        A2[(i, j)] = a2

ans = 0

