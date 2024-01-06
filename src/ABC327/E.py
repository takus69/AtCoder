N = int(input())
P = list(map(int, input().split()))

# i回目のコンテストまで参加して、j個を選択した時の最大値
dp = [[0 for j in range(i+1)] for i in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if i > j:
            a = dp[i-1][j]
        else:
            a = 0
        b = dp[i-1][j-1]*0.9 + P[i-1]
        dp[i][j] = max(a, b)
ans = -1200
for j in range(1, N+1):
    R = dp[N][j]/sum([0.9**(j-i-1) for i in range(j)]) - 1200/(j**(1/2))
    ans = max(R, ans)
# print(dp)
print(ans)
