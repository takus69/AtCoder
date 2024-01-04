n = int(input())
v = list(map(int, input().split()))

cnt1 = {}
cnt2 = {}
for i in range(n):
    vi = v[i]
    if i%2==0:
        cnt2[vi] = cnt2.get(vi, 0)+1
    else:
        cnt1[vi] = cnt1.get(vi, 0)+1
c1 = sorted([(k, v) for k, v in cnt1.items()], key=lambda x: x[1], reverse=True)[:2]
if len(c1) > 1:
    c1_1, c1_2 = c1
else:
    c1_1 = c1[0]
    c1_2 = (-1, -1)
c2 = sorted([(k, v) for k, v in cnt2.items()], key=lambda x: x[1], reverse=True)[:2]
if len(c2) > 1:
    c2_1, c2_2 = c2
else:
    c2_1 = c2[0]
    c2_2 = (-1, -1)

if c1_1[0] != c2_1[0]:
    ans = (n//2-c1_1[1]) + (n//2-c2_1[1])
else:
    ans = min((n//2-c1_1[1]) + (n//2-c2_2[1]), (n//2-c1_2[1]) + (n//2-c2_1[1]), (n//2-c1_1[1])+(n//2), (n//2)+(n//2-c2_1[1]))
print(ans)
