import bisect


N = int(input())
A = list(map(int, input().split()))

inds = {}
for i in range(N):
    if A[i] in inds.keys():
        inds[A[i]].append(i)
    else:
        inds[A[i]] = [i]
# print(inds)

Q = int(input())
for _ in range(Q):
    L, R, X = map(int, input().split())
    ind = inds.get(X, [])
    n = len(ind)
    l, r = 0, n-1
    # 二分探索でL以上の最小を求める
    ll = bisect.bisect_left(ind, L-1)
    # 二分探索でR以上の最小を求める
    rr = bisect.bisect_right(ind, R-1)
    # print(ind, ll, rr)
    print(rr-ll)
