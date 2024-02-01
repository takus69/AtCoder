N = int(input())
X, Y = map(int, input().split())
AB = []
for _ in range(N):
    AB.append(list(map(int, input().split())))
dp = [[[301 for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]  # i番目の弁当まででxとy個食べられるの最小の購入する弁当の数dp[i][x][y]
dp[0][0][0] = 0
for i in range(1, N+1):
    Ai, Bi = AB[i-1]
    for x in range(X+1):
        for y in range(Y+1):
            dp[i][x][y] = min(dp[i-1][x][y], dp[i][x][y])
            x2 = min(X, x+Ai)
            y2 = min(Y, y+Bi)
            dp[i][x2][y2] = min(dp[i-1][x2][y2], dp[i-1][x][y]+1, dp[i][x2][y2])
# for i in range(N+1):
#     print(dp[i])
ans = dp[N][X][Y]
if ans == 301:
    ans = -1
print(ans)
