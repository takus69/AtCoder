import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A)
keys = sorted(c.keys(), reverse=True)
sum_a = {}
pre_sum = 0
pre_key = max(keys)+1
flg = True
for k in keys:
    cnt = c[k]
    if pre_key == k+1:
        pre_sum += k*cnt
    else:
        flg = False
        pre_sum = k*cnt
    sum_a[k] = [pre_sum, flg]
    pre_key = k
sum_all = sum(A)
flg0 = False
if 0 in keys:
    flg0 = sum_a[0][1]
    sum_0 = sum_a[0][0]
else:
    sum_0 = 0

ans = sum_all
tmp = sum_all
for k in keys:
    if flg0:
        ans = 0
    else:
        tmp = sum_all - sum_a[k][0]
        if sum_a[k][1]:
            tmp -= sum_0
    # print(tmp)
    if tmp < ans:
        ans = tmp
# print(sum_a)
print(ans)
