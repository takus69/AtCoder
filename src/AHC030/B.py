from dataclasses import dataclass
import sys
import numpy as np
import random
import itertools
import math


@dataclass
class Pos:
    i: int
    j: int


@dataclass
class Polyomino:
    d: int
    poses: list[Pos]


class Judge:

    def __init__(self):
        self.N, self.M, self.e = self._read_initial()
        self.oil_fields = []
        for _ in range(self.M):
            self.oil_fields.append(self._read_oil_field())
        self.cost = 0
    
    def read_initial(self) -> list[int, int, int]:
        return self.N, self.M, self.e

    def read_oil_fields(self) -> list[Polyomino]:
        return self.oil_fields

    def _read_initial(self) -> Polyomino:
        tmp = input().split()
        N, M, e = int(tmp[0]), int(tmp[1]), float(tmp[2])
        return N, M, e

    def _read_oil_field(self) -> Polyomino:
        dij = list(map(int, input().split()))
        d = dij[0]
        ij = dij[1:]
        poses = []
        for i in range(0, len(ij), 2):
            poses.append(Pos(ij[i], ij[i+1]))
        return Polyomino(d, poses)

    def query(self, poly: Polyomino) -> int:
        self.cost += 1/(poly.d**(1/2))
        s = f'q {poly.d}'
        for p in poly.poses:
            s += f' {p.i} {p.j}'
        print(s)
        return int(input())

    def answer(self, poses: list[Pos]) -> int:
        s = f'a {len(poses)}'
        for p in poses:
            s += f' {p.i} {p.j}'
        print(s)
        return int(input())

    def comment(self, message: str) -> None:
        print(f'# {message}')

    def color(self, p:  Pos, c: str) -> None:
        print(f'#c {p.i} {p.j} {c}')


class Solver:

    def __init__(self):
        self.judge = Judge()
        self.N, self.M, self.e = self.judge.read_initial()
        self.oil_fields = self.judge.read_oil_fields()

    def solve(self) -> dict:
        # 配置の全パターンを列挙
        self.sum_d = 0
        self.max_i = [0 for _ in range(self.M)]
        self.max_j = [0 for _ in range(self.M)]
        self.M_pos = []
        for m in range(self.M):
            poly = self.oil_fields[m]
            self.sum_d += poly.d
            tmp = [[0]*self.N for _ in range(self.N)]
            for pos in poly.poses:
                self.max_i[m] = max(self.max_i[m], pos.i)
                self.max_j[m] = max(self.max_j[m], pos.j)
                tmp[pos.i][pos.j] += 1
            self.M_pos.append(tmp)
        self.M_cnt = []
        for m in range(self.M):
            self.M_cnt.append((self.N-self.max_i[m]) * (self.N-self.max_j[m]))
        self.pattern = list(itertools.product(*[range(self.M_cnt[m]) for m in range(self.M)]))
        Q_cnt = len(self.pattern)
        self.prob_Q = [1/Q_cnt for _ in self.pattern]

        # メイン処理
        random.seed(0)
        while True:
            trial_p = []
            poses = []
            # 占う場所を設定
            for m in range(self.M):
                p = random.randint(0, self.M_cnt[m]-1)
                trial_p.append(p)
                for pos in self.oil_fields[m].poses:
                    poses.append(Pos(pos.i+(p//(self.N-self.max_j[m])), pos.j+(p%(self.N-self.max_j[m]))))
            # 重複の場所を削除
            poses = sorted(poses, key=lambda x: (x.i, x.j))
            pre_i, pre_j = -1, -1
            tmp = []
            for pos in poses:
                if pos.i == pre_i and pos.j == pre_j:
                    continue
                tmp.append(pos)
                pre_i, pre_j = pos.i, pos.j
            poses = tmp

            v = self._mining(poses)
            self._update_prob(v, poses)
            if max(self.prob_Q) > 0.9:
                ret = self._answer()
                if ret == 1:
                    break
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'd': self.sum_d, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, poses: list[Pos]) -> int:
        d = len(poses)
        v = self.judge.query(Polyomino(d, poses))
        # self.judge.comment(f'mining: v={v}, poses={poses}')
        return v

    def _update_prob(self, v: float, poses: list[Pos]) -> None:
        prob_v_Q = []
        for pp in self.pattern:
            tmp = 0
            for m in range(self.M):
                p = pp[m]
                for pos in poses:
                    i2 = pos.i-(p//(self.N-self.max_j[m]))
                    j2 = pos.j-(p%(self.N-self.max_j[m]))
                    if 0 <= i2 < self.N and 0 <= j2 < self.N:
                        tmp += self.M_pos[m][i2][j2]
            prob_v_Q.append(self._gauss_dist(v, (len(poses)-tmp)*self.e+tmp*(1-self.e), len(poses)*self.e*(1-self.e)))
        prob_v = sum([prob_v_Q[i]*self.prob_Q[i] for i in range(len(prob_v_Q))])
        for i in range(len(self.pattern)):
            self.prob_Q[i] = self.prob_Q[i] * prob_v_Q[i] / prob_v
        
    def _gauss_dist(self, x: float, m: float, s2: float):
        ret = 1/(2*math.pi*s2)**(1/2)
        ret *= math.exp(-(x-m)**2/(2*s2))
        return ret

    def _answer(self) -> None:
        max_i, max_prob = 0, 0
        for i in range(len(self.pattern)):
            if max_prob < self.prob_Q[i]:
                max_prob = self.prob_Q[i]
                max_i = i
        poses = []
        for m in range(self.M):
            p = self.pattern[max_i][m]
            for pos in self.oil_fields[m].poses:
                poses.append(Pos(pos.i+(p//(self.N-self.max_j[m])), pos.j+(p%(self.N-self.max_j[m]))))
        # 重複の場所を削除
        poses = sorted(poses, key=lambda x: (x.i, x.j))
        pre_i, pre_j = -1, -1
        tmp = []
        for pos in poses:
            if pos.i == pre_i and pos.j == pre_j:
                continue
            tmp.append(pos)
            pre_i, pre_j = pos.i, pos.j
        poses = tmp
        ret = self.judge.answer(poses)
        if ret == 0:
            self.prob_Q[max_i] = 0
        return ret


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
