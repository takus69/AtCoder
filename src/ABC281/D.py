N, K, D = map(int, input().split())
a = list(map(int, input().split()))

# aiからj個選ばれて、余りがkでDP
dp = [[[-1 for k in range(D)] for j in range(K+1)] for i in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(min(K+1, i+1)):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            # aiを選ばない場合
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            # aiを選ぶ場合
            if j < K:
                dp[i+1][j+1][(k+a[i])%D] = max(dp[i+1][j+1][(k+a[i])%D], dp[i][j][k]+a[i])
print(dp[N][K][0])
