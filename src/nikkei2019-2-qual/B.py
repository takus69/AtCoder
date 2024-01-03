N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

max_D = max(D)
cnt = {i: 0 for i in range(max_D+1)}
for d in D:
    cnt[d] += 1
if D[0] == 0 and cnt[0] == 1:
    ans = 1
else:
    ans = 0
pre_cnt = 1
for i in range(1, max_D+1):
    # print(pre_cnt, cnt[i])
    if cnt[i] == 0 or ans == 0:
        ans = 0
        break
    else:
        ans *= pow(pre_cnt, cnt[i], MOD)
        ans %= MOD
    pre_cnt = cnt[i]
print(ans)
