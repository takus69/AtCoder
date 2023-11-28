L, N1, N2 = map(int, input().split())
v1, l1 = [], []
v2, l2 = [], []
for _ in range(N1):
    v, l = map(int, input().split())
    v1.append(v)
    l1.append(l)
for _ in range(N2):
    v, l = map(int, input().split())
    v2.append(v)
    l2.append(l)

ans = 0
i1, i2 = 0, 0
L1, L2 = 0, 0
while True:
    if i1 >= N1 or i2 >= N2:
        break
    vv1 = v1[i1]
    ll1 = l1[i1]
    vv2 = v2[i2]
    ll2 = l2[i2]
    mv = min(ll1, ll2)
    # print(vv1, ll1, vv2, ll2, mv)
    if vv1 == vv2:
        ans += mv
        if ll1 < ll2:
            i1 += 1
            l2[i2] -= mv
        elif ll1 > ll2:
            i2 += 1
            l1[i1] -= mv
        else:
            i1 += 1
            i2 += 1
    elif ll1 < ll2:
        i1 += 1
        l2[i2] -= mv
    else:
        i2 += 1
        l1[i1] -= mv
print(ans)
