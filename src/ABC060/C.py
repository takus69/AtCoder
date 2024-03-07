N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
pre_ti = -T
for ti in t:
    if pre_ti + T > ti:
        ans -= pre_ti+T-ti
    ans += T
    pre_ti = ti
print(ans)
