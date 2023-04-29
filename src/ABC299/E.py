from collections import deque


N, M = map(int, input().split())
uv = []
for _ in range(M):
    uv.append(list(map(int, input().split())))
K = int(input())
pd = []
for _ in range(K):
    pd.append(list(map(int, input().split())))

g = {i: [] for i in range(N)}
for u, v in uv:
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def bfs(u):
    queue = deque([u])
    d = {i: None for i in range(N)}
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

dd = {}
for i in range(N):
    dd[i] = bfs(i)

ans = 'Yes'
v = {i: 1 for i in range(N)}
# d未満はすべて白(0)にする
for p, d in pd:
    for i in range(N):
        if dd[p-1][i] < d:
            v[i] = 0
# dに黒(1)が1つでもあることを確認する
for p, d in pd:
    flg = False
    for i in range(N):
        if dd[p-1][i] == d:
            if v[i] == 1:
                flg = True
    if not flg:
        ans = 'No'
        break

S = ''
for i in range(N):
    S += str(v[i])
if S == '0'*N:
    ans = 'No'
if ans == 'No':
    print(ans)
else:
    print(ans)
    print(S)