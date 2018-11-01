def run(N, Q, P):
    union_find = UnionFind(N)
    ret = []
    for i in range(Q):
        p = P[i][0]
        a = P[i][1]
        b = P[i][2]
        if p == 0:
            union_find.unite(a, b)
        else:
            if union_find.same(a, b):
                ret.append('Yes')
            else:
                ret.append('No')
    return ret


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


def main():
    N, Q = map(int, input().split())
    P = []
    for i in range(Q):
        P.append(list(map(int, input().split())))
    for ret in run(N, Q, P):
        print(ret)


if __name__ == '__main__':
    main()
