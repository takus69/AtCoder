N = int(input())
S = input()
Q = int(input())
cd = {}
for _ in range(Q):
    c, d = input().split()
    if c in cd.keys():
        None
    else:
        cd[c] = d
    for k, v in cd.items():
        if v == c:
            cd[k] = d
ans = ''
for s in S:
    ans += cd.get(s, s)
print(ans)
