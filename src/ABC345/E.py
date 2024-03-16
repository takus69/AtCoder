N, K = map(int, input().split())
C, V = [], []
for _ in range(N):
    c, v = map(int, input().split())
    C.append(c)
    V.append(v)
ans = 0
pre_c = 0
pre_v = 0
Vs = []
Cs = []
for i in range(N):
    c, v = C[i], V[i]
    if pre_c == c:
        K -= 1
        if pre_v < v:
            ans -= pre_v
            ans += v
            pre_v = v
            Vs[-1] = v
    else:
        ans += v
        Vs.append(v)
        Cs.append(c)
        pre_v = v
    pre_c = c
    # print('ans', i, ans)
    if K < 0:
        ans = -1
        break
C2 = set(C)
if K > 0:
    dp = [{c: -1 for c in C2} for _ in range(K+1)]  # k個除外で、C2の順でその色で終わる最大の価値。-1は対象無し
    for i in range(len(Vs)):
        # print(dp)
        v, c = Vs[i], Cs[i]
        if dp[0][c] < 0:
            dp[0][c] = v
            dp[1][c] = 0
        for k in range(K+1):
            for c2 in C2:
                if c2 == c:
                    continue
                if dp[k][c2] < 0:
                    continue
                dp[k][c] = max(dp[k][c], dp[k][c2]+v)
                if k < K:
                    dp[k+1][c] = max(dp[k+1][c], dp[k+1][c2]+v)
    ans = max(dp[K].values())
    # print(dp)

print(ans)
