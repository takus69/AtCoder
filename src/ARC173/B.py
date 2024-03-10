N = int(input())
xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))
max_cnt = 0
for i in range(N):
    xi, yi = xy[i]
    for j in range(N):
        xj, yj = xy[j]
        if i == j:
            continue
        yji = yj-yi
        xji = xj-xi
        cnt = 2
        for k in range(N):
            if i == k or j == k:
                continue
            xk, yk = xy[k]
            if yji*(xk-xi) == xji*(yk-yi):
                cnt += 1
        max_cnt = max(cnt, max_cnt)
# print(N, max_cnt)
if max_cnt//2 > N-max_cnt:
    ans = N-max_cnt
else:
    ans = N//3
print(ans)
