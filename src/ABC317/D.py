N = int(input())

# i番目までで、対象の議席数までに鞍替えさせる必要がある人数の最低人数
INF = 10**12
dp = [[INF]*(10**5+1) for _ in range(N+1)]
dp[0][0] = 0
sum_Z = 0

for i in range(N):
    X, Y, Z = map(int, input().split())
    XX = (X+Y)//2+1-X
    sum_Z += Z
    if XX < 0:
        XX = 0
    for j in range(10**5+1):
        pre = dp[i][j]
        if pre < INF:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            ZZ = j+Z
            if ZZ > 10**5+1:
                ZZ = 10**5
            dp[i+1][ZZ] = min(dp[i][j]+XX, dp[i+1][ZZ])
print(min(dp[N][sum_Z//2+1:]))
