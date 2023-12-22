N, M = map(int, input().split())
name = input()
kit = input()

c_cnt = {}
for c in name:
    c_cnt[c] = c_cnt.get(c, 0) + 1
k_cnt = {}
for k in kit:
    k_cnt[k] = k_cnt.get(k, 0) + 1
ans = 0
for c, cnt in c_cnt.items():
    if c not in k_cnt.keys():
        ans = -1
        break
    else:
        ans = max(ans, (cnt-1) // k_cnt[c] + 1)

print(ans)
