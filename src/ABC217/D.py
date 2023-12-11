from sortedcontainers import SortedSet

L, Q = map(int, input().split())
X = SortedSet([0, L])
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        X.add(x)
    else:
        l = X.bisect_left(x)
        print(X[l]-X[l-1])
