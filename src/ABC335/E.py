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
target = [1]
for i, a in sorted(enumerate(A), key=lambda x: x[1]):
    if a < A[0] or i == 0:
        continue
    target.append(i+1)

E = {i+1: [] for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    if A[u-1] == A[v-1]:
        uf.unite(u, v)
    # print(u, v, vp)
    if A[u-1] > A[v-1]:
        u, v = v, u
    E[u].append(v)
# print(vp)
dp = {uf.root(1): 1}  # 頂点iにいる時の最大の種類数
for u in target:
    for v in E[u]:
        u = uf.root(u)
        v = uf.root(v)
        if A[u-1] < A[v-1] and dp.get(u, 0) > 0:
            dp[v] = max(dp.get(u, 0)+1, dp.get(v, 0))
            # print(u, v, A[u-1], A[v-1], dp)
# print(dp)
print(dp.get(uf.root(N), 0))
