N, M = map(int, input().split())
dp = {-1: 0, 0: 1}
now = 0
a = []
for _ in range(M):
    a.append(int(input()))
a = set(a)
for now in range(1, N+1):
    if now in a:
        dp[now] = 0
    else:
        dp[now] = (dp[now-2] + dp[now-1])%1000000007 

print(dp[N])
