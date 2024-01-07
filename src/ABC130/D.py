N, K = map(int, input().split())
a = list(map(int, input().split()))

sum_a = [0]
for ai in a:
    sum_a.append(sum_a[-1]+ai)

ans = 0
l, r = 0, 1
while r <= N:
    # print(r, l, sum_a[r]-sum_a[l], K)
    if sum_a[r]-sum_a[l] >= K:
        ans += N-r+1
        l += 1
    else:
        r += 1
# print(sum_a)
print(ans)
