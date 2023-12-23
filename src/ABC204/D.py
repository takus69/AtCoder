N = int(input())
T = list(map(int, input().split()))

S = sum(T)
# dp[i][j]: Tを順にi個まで使って、合計がjになるかどうか。j <= 10^3(Nの最大)*10^2(Tの最大)となるためメモリに収まる
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    Ti = T[i-1]
    for j in range(S+1):
        if dp[i-1][j]:
            dp[i][j] = True
            if j + Ti <= S:
                dp[i][j+Ti] = True

end_flag = False
for j in range(S//2 + S%2, S+1):
    for i in range(1, N+1):
        # print(i, j, dp[i][j])
        if dp[i][j]:
            print(j)
            end_flag = True
            break
    if end_flag:
        break
# print(dp)

''' 間違った最初の解答
T = sorted(T, reverse=True)
print(T)

oven1, oven2 = 0, 0
for t in T:
    if oven1 <= oven2:
        oven1 += t
    else:
        oven2 += t

print(max(oven1, oven2))
'''
