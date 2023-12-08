# dp[i][c]: i回目のコイントスで、カウンタがcの際の最大値
N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = {}
for _ in range(M):
    C, Y = map(int, input().split())
    CY[C] = Y

dp = [[0]]
for i in range(1, N+1):
    dp.append([])
    dp[i].append(max([c2 for c2 in dp[i-1]]))
    c = 0
    for xy in dp[i-1]:
        c += 1
        # print(i, c, ':', dp[(i-1, c-1)], X[i-1], CY.get(c, 0))
        dp[i].append(xy + X[i-1] + CY.get(c, 0))

ans = max([c2 for c2 in dp[N]])
# print(dp)
print(ans)
