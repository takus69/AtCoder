N = int(input())
A = list(map(int, input().split()))
pre = A[0]
l = {pre: None}
r = {A[-1]: None}
for a in A[1:]:
    l[a] = pre
    r[pre] = a
    pre = a
# print('l', l)
# print('r', r)

start = A[0]
Q = int(input())
for _ in range(Q):
    t = list(map(int, input().split()))
    q = int(t[0])
    if q == 1:
        x, y = t[1:]
        if r[x] is not None:
            l[r[x]] = y
        l[y] = x
        r[y] = r[x]
        r[x] = y
    else:
        x = t[1]
        if start == x:
            start = r[x]
        if l[x] is not None:
            r[l[x]] = r[x]
        if r[x] is not None:
            l[r[x]] = l[x]
        del r[x]
        del l[x]
ans = []
while start is not None:
    ans.append(start)
    start = r[start]
print(' '.join(map(str, ans)))
