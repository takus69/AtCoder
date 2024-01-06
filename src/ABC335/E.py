from queue import Queue

class UnionFind():
    '''Union find(ランクなし)'''
    def __init__(self, n):
        self.par = []
        for i in range(n):
            self.par.append(i)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x_root = self.root(self.par[x])
        y_root = self.root(self.par[y])
        if x_root == y_root:
            pass
        else:
            self.par[x_root] = y_root

    def same(self, x, y):
        return self.root(x) == self.root(y)

N, M = map(int, input().split())
A = list(map(int, input().split()))
# 同じ値で連結している場合をUnionFindで管理
uf = UnionFind(N+1)
uv = []
for _ in range(M):
    u, v = map(int, input().split())
    if A[u-1] == A[v-1]:
        if uf.root(u) == 1:
            u, v = v, u
        uf.unite(u, v)
    uv.append((u, v))
E = {i: [] for i in range(1, N+1)}
for u, v in uv:
    u = uf.root(u)
    v = uf.root(v)
    if u == v:
        continue
    E[u].append(v)
    E[v].append(u)
# for k, v in E.items():
#     E[k] = list(set(E[k]))
# print(E)

cnt = 0
dp = {1: 1}  # 頂点iにいる時の最大の種類数
q = Queue()
pre = uf.root(1)
for v in E[1]:
    v = uf.root(v)
    if v != 1 and v != pre and A[pre-1] < A[v-1]:
        cnt += 1
        q.put((1, v))
while not q.empty():
    pre, u = q.get()
    u = uf.root(u)
    if A[pre-1] < A[u-1]:
        dp[u] = max(dp[pre]+1, dp.get(u, 0))
    else:
        dp[u] = dp.get(u, 0)

    # 次のキューを入れる
    for v in E[u]:
        if v != u and v != pre and A[u-1] < A[v-1]:
            cnt += 1
            q.put((u, v))
# print(dp, uf.root(N), cnt)
print(dp.get(uf.root(N), 0))
