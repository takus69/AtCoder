import unittest
from A import Pos, Judge, Solver
from test_A import MockJudge
from typing import List
import math
import os
import numpy as np


class TestA(unittest.TestCase):
    def test_simulator(self):
        files = os.listdir('in')
        scores = []
        W_Ns = []
        for filename in files:
            score, W, N = self.all_run(os.path.join('in', filename), os.path.join('out', filename))
            scores.append(score)
            W_Ns.append(W/N)
        print('score:', np.mean(scores), '±', np.std(scores))
        print('W/N:', np.mean(W_Ns), '±', np.std(W_Ns))

    def all_run(self, in_filename, out_filename):
        out_f = open(out_filename, 'w')
        in_f = open(in_filename, 'r')
        L, N, S = [int(v) for v in in_f.readline().split(' ')]
        landing_pos = []
        for _ in range(N):
            y, x = (int(v) for v in in_f.readline().split(' '))
            landing_pos.append(Pos(y, x))
        A = []
        for _ in range(N):
            A.append(int(in_f.readline()))
        f = []
        for _ in range(10000):
            f.append(int(in_f.readline()))
        in_f.close()

        judge = MockJudge(A, f, landing_pos, out_f, display=False)
        solver = Solver(L, N, S, landing_pos, judge, display=False)
        solver.solve()
        out_f.close()
        return judge.evaluate()
        


if __name__ == '__main__':
    unittest.main()
