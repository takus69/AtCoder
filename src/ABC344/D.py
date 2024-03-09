T = input()
N = int(input())
A = []
S = []
for _ in range(N):
    tmp = input().split()
    A.append(int(tmp[0]))
    S.append(tmp[1:])

ans = N+1
dp = [{T[:i]: N+1 for i in range(len(T)+1)} for _ in range(N+1)]
# print(dp)
# print(used)
# print(S)
dp[0][''] = 0
for i in range(1, N+1):
    for j in range(A[i-1]):
        s = S[i-1][j]
        for k, v in dp[i-1].items():
            if v < 0:
                continue
            dp[i][k] = min(dp[i][k], v)
            if T.startswith(k+s):
                dp[i][k+s] = min(dp[i][k+s], dp[i-1][k] + 1)
            if T == k+s:
                ans = min(dp[i][k+s], ans)

if ans == N+1:
    ans = -1
print(ans)
