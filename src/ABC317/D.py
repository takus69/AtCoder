N = int(input())

# i番目までで、対象の議席数までに鞍替えさせる必要がある人数の最低人数
sum_Z = 0
max_XY = 0

XYZ = []
for i in range(N):
    X, Y, Z = map(int, input().split())
    XYZ.append((X, Y, Z))
    sum_Z += Z
    max_XY += X+Y

INF = max_XY + 1
dp = [[INF]*(sum_Z+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    X, Y, Z = XYZ[i]
    XX = (X+Y)//2+1-X
    if XX < 0:
        XX = 0
    for j in range(sum_Z+1):
        # print(i, j, Z)
        pre = dp[i][j]
        if pre < INF:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            ZZ = j+Z
            if ZZ > sum_Z:
                ZZ = sum_Z
            dp[i+1][ZZ] = min(dp[i][j]+XX, dp[i+1][ZZ])
# print(dp)
print(min(dp[N][sum_Z//2+1:]))
