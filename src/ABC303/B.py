N, M = map(int, input().split())
a = []
for i in range(M):
    a.append(list(map(int, input().split())))

c = {}
for i in range(N-1):
    for j in range(i+1, N):
        c[(i, j)] = 0
for i in range(M):
    for j in range(N-1):
        a1, a2 = a[i][j]-1, a[i][j+1]-1
        a1, a2 = min(a1, a2), max(a1, a2)
        c[(a1, a2)] = 1
# print(c)

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if c[(i, j)] == 0:
            ans += 1

print(ans)
