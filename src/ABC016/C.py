N, M = map(int, input().split())

fri = {i+1: [] for i in range(N)}
for _ in range(M):
    a, b = list(map(int, input().split()))
    fri[a].append(b)
    fri[b].append(a)

frifri = {i+1: [] for i in range(N)}
for k, v in fri.items():
    for b in v:
        frifri[k] = frifri.get(k) + fri[b]

for i in range(N):
    k = i+1
    v = frifri[k]
    cnt = 0
    for b in set(v):
        # print(k, b)
        if k != b and b not in fri[k]:
            cnt += 1
    print(cnt)
# print(fri, frifri)
