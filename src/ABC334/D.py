import bisect


N, Q = map(int, input().split())
R = list(map(int, input().split()))
R = sorted(R)
sum_R = []
tmp_sum_R = 0
for r in R:
    tmp_sum_R += r
    sum_R.append(tmp_sum_R)
for _ in range(Q):
    X = int(input())
    i = bisect.bisect_right(sum_R, X)
    print(i)
