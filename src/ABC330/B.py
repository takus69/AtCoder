N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a in A:
    if L <= a and a <= R:
        ans.append(a)
    else:
        if abs(L-a) <= abs(R-a):
            ans.append(L)
        else:
            ans.append(R)

print(' '.join(map(str, ans)))
