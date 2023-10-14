import random


random.seed(0)

class Solver:
    def __init__(self):
        # 初期設定
        self.N, self.D, self.Q = map(int, input().split())
        self.ans = [d for d in range(self.D)]
        self.ans += [random.randint(0, self.D-1) for _ in range(self.D, self.N)]
        print('#C', ' '.join(map(str, self.ans)))
        self.q_cnt = 0  # クエリの回数

    # 関数定義
    def measure_d(self, dl, dr):
        '''
        D個の集合同士の比較
        '''
        nl = 0
        nr = 0
        l = []
        r = []
        for i in range(self.N):
            d = self.ans[i]
            if d == dl:
                nl += 1
                l.append(i)
            elif d == dr:
                nr += 1
                r.append(i)
        print(' '.join(map(str, [nl, nr] + l + r)))
        q = input()
        print('# {} {} {}'.format(dl, q, dr))
        self.q_cnt += 1
        return q

    def measure_n(self, i1, i2):
        print('1 1 {} {}'.format(i1, i2))
        q = input()
        print('# {} {} {}'.format(i1, q, i2))
        self.q_cnt += 1
        return q

    def switch(self, i1, i2):
        d1 = self.ans[i1]
        d2 = self.ans[i2]
        self.ans[i1] = d2
        self.ans[i2] = d1

    def solve(self):
        while self.q_cnt < self.Q:
            # Dの集合の比較
            dl = random.randint(0, self.D-1)
            dr = dl
            while dr == dl:
                dr = random.randint(0, self.D-1)
            q_d = self.measure_d(dl, dr)
            if self.q_cnt >= self.Q:
                break
            if q_d == '=':
                continue
            
            # 要素の比較
            dl_n = []
            dr_n = []
            for j in range(self.N):
                if self.ans[j] == dl:
                    dl_n.append(j)
                elif self.ans[j] == dr:
                    dr_n.append(j)
            nl = random.choice(dl_n)
            nr = random.choice(dr_n)
            q_n = self.measure_n(nl, nr)
            if q_d == q_n:
                self.switch(nl, nr)
            print('#C', ' '.join(map(str, self.ans)))

        print(' '.join(map(str, self.ans)))


if __name__ == '__main__':
    solver = Solver()
    solver.solve()

