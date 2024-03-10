T = int(input())
dp = [1, 9]  # i桁のNeq Numberの数
for i in range(1, 12):
    dp.append(dp[i]*8 + dp[i-1]*9)
# print(dp)
for _ in range(T):
    K = int(input())
    d = 1  # 桁数
    for c in dp[1:]:
        if K - c <= 0:
            break
        else:
            K -= c
            d += 1
    ans = [0]
    # 上から順に桁の数値を決定
    for i in range(d-1):
        if i > 0 and ans[-1] > 0:
            tmp = 0
            c = dp[d-i-1]
        else:
            tmp = 1
            c = dp[d-i-1]*8//9 + dp[d-i-2]
        while K - c > 0:
            if tmp == ans[-1]:
                tmp += 1
                continue
            K -= c
            tmp += 1
            c = dp[d-i-1]*8//9 + dp[d-i-2]
        if tmp == ans[-1]:
            tmp += 1
        ans.append(tmp)
    for i in range(10):
        if i != ans[-1]:
            K -= 1
        if K == 0:
            ans.append(i)
            break
    print(''.join(map(str, ans[1:])))
