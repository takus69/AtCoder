import sys

sys.setrecursionlimit(100000)


H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

MOD = 998244353

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

uf = UnionFind(H*W)

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            uf.root(W*i + j)
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                i2, j2 = i+di, j+dj
                if 0 <= i2 < H and 0 <= j2 < W:
                    if S[i2][j2] == '#':
                        uf.unite(W*i+j, W*i2+j2)
roots = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            roots.append(uf.root(W*i+j))
cnt = len(set(roots))
# print(roots, cnt)
red_cnt = 0
join_cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            red_cnt += 1
            join = []
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                i2, j2 = i+di, j+dj
                if 0 <= i2 < H and 0 <= j2 < W:
                    if S[i2][j2] == '#':
                        join.append(uf.root(W*i2+j2))
            cnt2 = len(set(join))
            # print(cnt, cnt2)
            join_cnt += cnt - cnt2 + 1

def gcd(x, y):
    '''ユークリッド互除法'''
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

def modint(P, Q, MOD):
    '''有理数P/QのMODを算出'''
    return (P * pow(Q, -1, MOD)) % MOD

# print(join_cnt, red_cnt)
# print(gcd(join_cnt, red_cnt))
print(modint(join_cnt, red_cnt, MOD))
