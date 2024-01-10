N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

# (i, ci)までの組み合わせの累積和
dp = [{} for _ in range(N)]
dp[0] = {ci: ci-a[0]+1 for ci in range(a[0], b[0]+1)}
for i in range(1, N):
    sum_ci = 0
    for ci in range(a[i], b[i]+1):
        tmp = dp[i-1][b[i-1]]
        # print(i, ci, tmp)
        if ci in dp[i-1].keys():
            sum_ci += dp[i-1][ci]
            tmp = dp[i-1][ci]
        else:
            sum_ci += tmp

        sum_ci %= MOD
        dp[i][ci] = sum_ci

# print(dp)
print(dp[N-1][b[-1]])
