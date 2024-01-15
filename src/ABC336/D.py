N = int(input())
A = list(map(int, input().split()))

dp_l = [0]  # 左から見ていって、作れる最大
dp_r = [0]  # 右から見ていって、作れる最大
for i in range(N):
    dp_l.append(min(dp_l[i]+1, A[i], i+1))
    dp_r.append(min(dp_r[i]+1, A[-i-1], i+1))
# print(dp_l, dp_r)
ans = 0
for i in range(N):
    l = dp_l[i+1]
    r = dp_r[-i-1]
    # print(ans, l, r)
    ans = max(ans, min(l, r))

print(ans)
