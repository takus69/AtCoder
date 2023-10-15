import unittest
from A import Solver
import numpy as np


class TestA(unittest.TestCase):
    def test_w2d(self):
        solver = MockSolver('testcases/0001.txt', 'testcases/0001_out.txt')
        solver.solve()
        score1 = solver.evaluate()
        print(' '.join(map(str, solver.ans)))
        solver.w2d(solver.W)
        score2 = solver.evaluate()
        print(' '.join(map(str, solver.ans)))
        print(format(score1, ','), format(score2, ','))


class MockSolver(Solver):
    def __init__(self, in_file, out_file):
        self.out = None
        self.in_file = open(in_file, 'r')
        self.out_file = open(out_file, 'w')
        super().__init__()
        self.W = list(map(int, self.input().split()))

    def input(self):
        ret = self.out
        if ret is None:
            ret = self.in_file.readline()
        self.out = None
        return ret
    
    def print(self, s):
        # 出力を設定
        if not s.startswith('#'):
            tmp = list(map(int, s.split(' ')))
            nl, nr = tmp[0], tmp[1]
            l, r = tmp[2:2+nl], tmp[2+nl:]
            wl = 0
            for i in l:
                wl += self.W[i]
            wr = 0
            for i in r:
                wr += self.W[i]
            if wl > wr:
                self.out = '>'
            elif wl < wr:
                self.out = '<'
            else:
                self.out = '='
        self.out_file.write(s + '\n')
        if s.startswith('#c'):
            score = self.evaluate()
            self.out_file.write('# ' + str(score) + '\n')

    def submission(self):
        super().submission()
        if self.in_file is not None:
            self.in_file.close()
            self.out_file.close()

    def evaluate(self):
        Dw = [0 for _ in range(self.D)]
        for i in range(self.N):
            Dw[self.ans[i]] += self.W[i]
        score = 1 + round(np.std(Dw) * 100)
        return score


if __name__ == '__main__':
    solver = MockSolver('testcases/0000.txt', 'testcases/0000_out.txt')
    solver.solve()
    score = solver.evaluate()
    print(score)
