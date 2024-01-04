N = int(input())
TXA = {}
for _ in range(N):
    T, X, A = map(int, input().split())
    TXA[(T, X)] = A
MAX_T = max([t for t, x in TXA.keys()])
# print(MAX_T)

# dp[t][x]
dp = [[0]*5 for _ in range(MAX_T+1)]
next_moves = set([0, 1])
for t in range(1, MAX_T+1):
    tmp_moves = []
    for x in next_moves:
        if x-1 < 0:
            dp[t][x] = max(dp[t-1][x], dp[t-1][x+1])
        elif x+1 > 4:
            dp[t][x] = max(dp[t-1][x], dp[t-1][x-1])
        else:
            dp[t][x] = max(dp[t-1][x], dp[t-1][x-1], dp[t-1][x+1])
        if (t, x) in TXA.keys():
            dp[t][x] += TXA[(t, x)]
        tmp_moves.append(max(0, x-1))
        tmp_moves.append(min(4, x+1))
        tmp_moves.append(x)
    next_moves = set(tmp_moves)

ans = 0
for a in dp[MAX_T]:
    ans = max(ans, a)
print(ans)
