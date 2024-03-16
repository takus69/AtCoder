S = input()
d = {}

for s in S:
    d[s] = d.get(s, 0)+1
n = len(S)
ans = 0
flg = False
for k, v in d.items():
    ans += v*(n-v)
    if v > 1:
        flg = True
ans //= 2
if flg:
    ans += 1
print(ans)
