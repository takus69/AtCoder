import random
import numpy as np
import copy
import math
import time


random.seed(0)

class Solver:
    def __init__(self):
        # 初期設定
        self.measure_d_cnt = 0
        self.measure_n_cnt = 0
        self.query = ''
        self.N, self.D, self.Q = map(int, self.input().split())
        self.ans = []
        for d in range(self.D):
            self.ans += [d] * (self.N//self.D)
        self.ans += [d for d in range(self.D)]
        self.ans = self.ans[:self.N]
        self.q_cnt = 0  # クエリの回数
        self.measure = {}
        self.bigger_cnt = {i: 0 for i in range(self.N)}
        self.smaller_cnt = {i: 0 for i in range(self.N)}
        self.bigger_rate = 2
        self.d_diff = {i: 0 for i in range(self.D)}
        self.l = 100000
        self.a = 10**(-10)
        self.calc_w()
    
    # 関数定義
    def calc_w(self):
        self.order_w = []
        pre = self.l
        for i in range(self.N):
            y = (i+1) / self.N
            x = -math.log(1-y+self.a)*self.l
            cal = (self.l + x) * math.exp(-x/self.l)
            self.order_w.append((pre-cal)*self.N)
            pre = cal

    def measure_d(self, dl, dr):
        '''
        D個の集合同士の比較
        '''
        self.measure_d_cnt += 1
        self.print('# measure d {} {}'.format(dl, dr))
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
        query = ' '.join(map(str, [nl, nr] + l + r))
        if query in self.measure.keys():
            q = self.measure[query]
        else:
            self.print(query)
            q = self.input()
            self.measure[query] = q
            self.q_cnt += 1
            if q == '<':
                self.d_diff[dr] += 1
                self.d_diff[dl] -= 1
            elif q == '>':
                self.d_diff[dl] += 1
                self.d_diff[dr] -= 1
        self.print('#d {} {} {}'.format(dl, q, dr))
        return q

    def measure_n(self, i1, i2):
        self.measure_n_cnt += 1
        self.print('# measure n {} {}'.format(i1, i2))
        query = '1 1 {} {}'.format(i1, i2)
        if query in self.measure.keys():
            q = self.measure[query]
        else:
            self.print(query)
            q = self.input()
            self.measure[query] = q
            self.q_cnt += 1
        self.print('#n {} {} {}'.format(i1, q, i2))
        return q

    def swap(self, i1, i2):
        self.print('# swap {} {}'.format(i1, i2))
        d1 = self.ans[i1]
        d2 = self.ans[i2]
        self.ans[i1] = d2
        self.ans[i2] = d1
    
    def move(self, i, d):
        self.print('# move {} to {}'.format(i, d))
        self.ans[i] = d

    def solve(self):
        start_time = time.time()
        self.print('#c ' + ' '.join(map(str, self.ans)))
        while self.q_cnt < self.Q:
            if time.time() - start_time > 1.5:
                self.print('1 1 0 1')
                self.q_cnt += 1
            # 処理前の予測スコア
            # pre_score = self.estimate_score()

            # Dの集合の比較
            dl = random.randint(0, self.D-1)
            min_cnt = min(self.d_diff.values())
            #dl = random.choices([i for i in range(self.D)], weights=[self.d_diff[i] - min_cnt + 1 for i in range(self.D)])[0]
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
            # D個の大の要素の平準化
            swap_flag2 = False
            '''
            dl_n_big, dl_n_small = self.bigger_D(dl_n)
            dr_n_big, dr_n_small = self.bigger_D(dr_n)
            if q_d == '>':
                if len(dl_n_big) > self.bigger_rate and len(dr_n_small) > 0:
                    dl_n = copy.copy(dl_n_big)
                    dr_n = copy.copy(dr_n_small)
                    swap_flag2 = True
            elif q_d == '<':
                if len(dr_n_big) > self.bigger_rate and len(dl_n_small) > 0:
                    dl_n = copy.copy(dl_n_small)
                    dr_n = copy.copy(dr_n_big)
                    swap_flag2 = True
            if not swap_flag2:
                if len(dl_n_small) > 0:
                    dl_n = copy.copy(dl_n_small)
                if len(dr_n_small) > 0:
                    dr_n = copy.copy(dr_n_small)
            '''
            nl = random.choice(dl_n)
            nr = random.choice(dr_n)
            # 交換か移動する
            swap_flag = True
            if random.random() < 0.7 or swap_flag2:
                swap_flag = True
                # 交換のパターン
                if nl > nr:
                    q_n = self.measure_n(nr, nl)
                    tmp = ''
                    if q_n == '>':
                        tmp == '<'
                    elif q_n == '<':
                        tmp == '>'
                    q_n = tmp
                    self.print('# debug {} {} {}'.format(nl, q_n, nr))
                else:
                    q_n = self.measure_n(nl, nr)
                # 後続処理が出来ないためswap前に終了
                if self.q_cnt >= self.Q:
                    break
                if q_d == q_n:
                    self.swap(nl, nr)
            else:
                # 移動のパターン
                swap_flag = False
                if q_d == '>':
                    if len(dl_n) == 1:
                        continue
                    self.move(nl, dr)
                elif q_d == '<':
                    if len(dr_n) == 1:
                        continue
                    self.move(nr, dl)
            q_d2 = self.measure_d(dl, dr)
            self.print('#c ' + ' '.join(map(str, self.ans)))
            if q_d2 == '=':
                continue
            elif q_d != q_d2:  # 大小関係が違う場合は戻す
            # 予測スコアが改善しない場合は戻す
            # self.print('# before:after {}:{}'.format(pre_score, self.estimate_score()))
            #if pre_score < self.estimate_score():
                # 確率で元に戻さない
                #if random.random() < 0.1 and self.q_cnt < self.Q / 2:
                #    continue
                # 大小が変わる場合は元に戻す。ただし平準化の場合は戻さない
                if swap_flag and not swap_flag2:
                    self.swap(nl, nr)
                else:
                    if q_d == '>':
                        self.move(nl, dl)
                    elif q_d == '<':
                        self.move(nr, dr)
            self.print('#c ' + ' '.join(map(str, self.ans)))

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

    def estimate_score(self):
        # wの順位を予測
        diff = {}
        bigger, smaller = [], []
        for i in range(self.N):
            diff[i] = self.bigger_cnt[i] - self.smaller_cnt[i]
        diff = sorted(diff.items(), key=lambda x: x[1])

        # 順位に対してwを割り当てる
        self.estimate_w = []
        pre_v = 0
        cnt = 0
        ww = 0
        for k, v in diff:
            if pre_v != v:
                for _ in range(cnt):
                    self.estimate_w.append(ww/cnt)
                ww = self.order_w[k]
                cnt = 1
                pre_v = v
            else:
                ww += self.order_w[k]
                cnt += 1
        for _ in range(cnt):
            self.estimate_w.append(ww/cnt)

        # 割り当てたwに対してスコアを算出
        Dw = [0 for _ in range(self.D)]
        for i in range(self.N):
            Dw[self.ans[i]] += self.estimate_w[i]
        score = 1 + round(np.std(Dw) * 100)
        return score

    def bigger_D(self, d_n):
        '''
        大きい方からD*bigger_rate個の配列を返却。残りの配列も返却
        '''
        diff = {}
        bigger, smaller = [], []
        for i in range(self.N):
            diff[i] = self.bigger_cnt[i] - self.smaller_cnt[i]
        diff = sorted(diff.items(), key=lambda x: x[1], reverse=True)[:self.D*self.bigger_rate]
        check = set(k for k, v in diff)
        for i in d_n:
            if i in check:
                bigger.append(i)
            else:
                smaller.append(i)
        return bigger, smaller

    def post_input(self, out):
        if self.query.startswith('1 1 '):
            tmp = list(map(int, self.query.split()))
            nl, nr = tmp[2], tmp[3]
            if out == '>':
                self.bigger_cnt[nl] += 1
                self.smaller_cnt[nr] += 1
            elif out == '<':
                self.bigger_cnt[nr] += 1
                self.smaller_cnt[nl] += 1
        self.query = ''

    def input(self):
        ret = input()
        self.post_input(ret)
        return ret

    def pre_print(self, s):
        self.query = s

    def print(self, s):
        self.pre_print(s)
        print(s)
    
    def submission(self):
        self.print(' '.join(map(str, self.ans)))
        self.print('# bigger: {}'.format(self.bigger_cnt))
        self.print('# smaller: {}'.format(self.smaller_cnt))
        self.print('# estimate score: {}'.format(self.estimate_score()))
        self.print('# measure_d_cnt: {}, measure_n_cnt: {}'.format(self.measure_d_cnt, self.measure_n_cnt))


if __name__ == '__main__':
    solver = Solver()
    solver.solve()
