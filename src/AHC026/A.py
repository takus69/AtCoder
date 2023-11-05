n, m = map(int, input().split())
b = {}
for i in range(m):
    b[i] = list(map(int, input().split()))

vi = {}
for i in range(m):
    for v in b[i]:
        vi[v] = i

ans = []
cost = []
for v in range(1, n+1):
    i = vi[v]
    h = len(b[i])
    for j in range(h):
        v2 = b[i][j]
        if v2 == v:
            break
    if j+1 == h:
        ans.append([v, 0])
        b[i] = b[i][:-1]
        #print(v, 0)
    else:
        #print('i, j:', i, j)
        v2 = b[i][j+1]
        i2 = (i+1)%m
        ans.append([v2, i2+1])  # 隣に入れる
        #print(v2, i2+1)
        ans.append([v, 0])
        #print(v, 0)
        for vv in b[i][j+1:]:
            vi[vv] = i2
        b[i2] += b[i][j+1:]
        b[i] = b[i][:j]
        cost.append(h-j)

for a in ans:
    print('{} {}'.format(a[0], a[1]))
print('#cost:', sum(cost))
print('#score:', max(1, 10000 - sum(cost)))

