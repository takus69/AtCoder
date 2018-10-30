class UnionFind():
    def run(self, N, M, p, x):
        '''Union find(ランクなし)'''
        # 初期化。index0はとりあえず0で埋める
        self.part = []
        for i in range(N+1):
            self.part.append(i) 
        # 経路をまとめる
        for i in range(M):
            self.union(x[i][0], x[i][1])
        cnt = 0
        for i in range(1, N+1):
            if self.root(i) == self.root(p[i-1]):
                cnt += 1
        return cnt

    def root(self, x):
        if self.part[x] == x:
            return x
        else:
            # 経路圧縮
            self.part[x] = self.root(self.part[x])
            return self.part[x]
    
    def union(self, x, y):
        x_root = self.root(self.part[x])
        y_root = self.root(self.part[y])
        if x_root == y_root:
            pass
        else:
            self.part[x_root] = y_root


def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    x = []
    for i in range(M):
        x.append(list(map(int, input().split())))
    obj = UnionFind()
    print(obj.run(N, M, p, x))


if __name__ == '__main__':
    main()
