N, M, K = map(int, input().split())
# dp[i][j]:=数列の先頭から i 項まで決めた際に、総和が j であるような数列の決め方の総数
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for k in range(1, M+1):
        for j in range(K):
            # print(i, k, j)
            if j+k > K:
                break
            dp[i+1][j+k] += dp[i][j]
            dp[i+1][j+k] %= 998244353
# print(dp)
ans = sum(dp[N]) % 998244353
print(ans)
