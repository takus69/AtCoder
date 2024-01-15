N = input()

# 桁和sの時、d+1桁, 桁和i(9×14), 余りj(mod s), Nと同じフラグf

ans = 0
for s in range(1, 9*14+1):
    dp = [[[[0 for _ in range(2)] for _ in range(s)] for _ in range(s+1)] for _ in range(len(N)+1)]
    # print(len(dp), len(dp[0]), len(dp[0][0]), len(dp[0][0][0]))
    dp[0][0][0][1] = 1

    for d in range(len(N)):
        for i in range(s+1):
            for j in range(s):
                for f in range(2):
                    for t in range(10):
                        if i+t > s:
                            continue
                        ff = 0
                        if f == 1 and t > int(N[d]):
                            continue
                        elif f == 1 and t == int(N[d]):
                            ff = 1
                        # print(dp[d+1], i+t)
                        # print(dp[d+1][i+t], (10*j+t)%s)
                        # print(dp[d+1][i+t][(10*j+t)%s])
                        # print(d, i, j, f)
                        # print(d, i, j, f)
                        # print(d+1, i+t, (10*j+t)%s, ff)
                        dp[d+1][i+t][(10*j+t)%s][ff] += dp[d][i][j][f]

    ans += dp[len(N)][s][0][1] + dp[len(N)][s][0][0]

print(ans)
