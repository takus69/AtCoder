import random
import numpy as np


random.seed(0)

class Solver:
    def __init__(self):
        # 初期設定
        self.N, self.D, self.Q = map(int, self.input().split())
        self.ans = []
        for d in range(self.D):
            self.ans += [d] * (self.N//self.D)
        self.ans += [d for d in range(self.D)]
        self.ans = self.ans[:self.N]
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
        self.print(' '.join(map(str, [nl, nr] + l + r)))
        q = self.input()
        self.print('# {} {} {}'.format(dl, q, dr))
        self.q_cnt += 1
        return q

    def measure_n(self, i1, i2):
        self.print('1 1 {} {}'.format(i1, i2))
        q = self.input()
        self.print('# {} {} {}'.format(i1, q, i2))
        self.q_cnt += 1
        return q

    def swap(self, i1, i2):
        d1 = self.ans[i1]
        d2 = self.ans[i2]
        self.ans[i1] = d2
        self.ans[i2] = d1

    def solve(self):
        self.print('#c ' + ' '.join(map(str, self.ans)))
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
                self.swap(nl, nr)
            # swap後の大小確認
            if self.q_cnt >= self.Q:
                # 後続処理が出来ないため元に戻す
                self.swap(nl, nr)
                break
            q_d2 = self.measure_d(dl, dr)
            self.print('#c ' + ' '.join(map(str, self.ans)))
            if q_d2 == '=':
                continue
            elif q_d != q_d2:
                # 大小が変わる場合は元に戻す
                self.swap(nl, nr)

        self.submission()
    
    def w2d(self, W):
        Dw = [0 for _ in range(self.D)]
        w_i = np.argsort(W)[::-1]
        W_mean = np.mean(W) * self.N / self.D
        d_i = 0
        d_diff = 1
        ans = [-1 for _ in range(self.N)]
        cnt = 0
        cnt2 = 0
        while cnt < self.N:
            i = w_i[cnt]
            if Dw[d_i] < W_mean or cnt2 == self.D:
                ans[i] = d_i
                Dw[d_i] += W[i]
                d_i += d_diff
                cnt += 1
                if cnt2 < self.D:
                    cnt2 = 0
            else:
                d_i += d_diff
                cnt2 += 1
            if d_i >= self.D:
                d_diff = -1
                d_i += d_diff
            elif d_i < 0:
                d_diff = 1
                d_i += d_diff
        self.ans = ans

    def input(self):
        return input()

    def print(self, s):
        print(s)
    
    def submission(self):
        self.print(' '.join(map(str, self.ans)))


if __name__ == '__main__':
    solver = Solver()
    solver.solve()

