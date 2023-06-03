import copy

class UnionFind():
    '''Union find(ランクなし)'''
    def __init__(self, n):
        self.par = [0]
        for i in range(n):
            self.par.append(i+1)
        # print(self.par)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        # print(x, y)
        x_root = self.root(self.par[x])
        y_root = self.root(self.par[y])
        if x_root == y_root:
            pass
        else:
            self.par[x_root] = y_root

    def same(self, x, y):
        return self.root(x) == self.root(y)

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    uf.unite(u, v)

K = int(input())
ans = 'Yes'
xy = []
xy_check = []
for _ in range(K):
    x, y = map(int, input().split())
    xy.append((x, y))
    if uf.same(x, y):
        ans = 'No'
    xy_check.append((uf.root(x), uf.root(y)))
xy_check = set(xy_check)
# print(xy_check)

Q = int(input())
# print(uf.par)
for _ in range(Q):
    # print('ans', ans)
    ans2 = ans
    if ans == 'No':
        pass
    else:
        p, q = map(int, input().split())
        rp = uf.root(p)
        rq = uf.root(q)
        if (rp, rq) in xy_check or (rq, rp) in xy_check:
            ans2 = 'No'
    print(ans2)
