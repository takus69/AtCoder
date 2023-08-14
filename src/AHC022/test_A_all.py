import unittest
from A import Pos, Judge, Solver, Solver2
from test_A import MockJudge
from typing import List
import math
import os
import numpy as np
import pandas as pd


class TestA(unittest.TestCase):
    def test_simulator(self):
        results = {
            'L':[], 'N':[], 'S':[],
            'score mean':[], 'score std':[], 'W/N mean':[], 'W/N std':[],
            'landing cost mean':[], 'landing cost std':[], 'measure cost mean':[], 'measure cost std': []
        }
        Ls = [10, 25, 50]
        Ns = [60, 80, 100]
        Ss = [1, 9, 25, 49, 81, 400, 900]
        for L in Ls:
            for N in Ns:
                for S in Ss:
                    base_path = os.path.join('testcases', f'L{L}N{N}S{S}')
                    print(L, N, S)
                    score_mean, score_std, W_N_mean, W_N_std, l_mean, l_std, m_mean, m_std = self.run_all(base_path)
                    results['L'].append(L)
                    results['N'].append(N)
                    results['S'].append(S)
                    results['score mean'].append(score_mean)
                    results['score std'].append(score_std)
                    results['W/N mean'].append(W_N_mean)
                    results['W/N std'].append(W_N_std)
                    results['landing cost mean'].append(l_mean)
                    results['landing cost std'].append(l_std)
                    results['measure cost mean'].append(m_mean)
                    results['measure cost std'].append(m_std)
        pd.DataFrame(results).to_csv('results.csv')

    def run_all(self, base_path, in_param=None):
        files = os.listdir(os.path.join(base_path, 'in'))
        scores = []
        W_Ns = []
        l_costs = []
        m_costs = []
        for filename in files:
            score, W, N, landing_cost, measure_cost = self.run_one(os.path.join(base_path, 'in', filename), os.path.join(base_path, 'out', filename), in_param=in_param)
            scores.append(score)
            W_Ns.append(W/N)
            l_costs.append(landing_cost)
            m_costs.append(measure_cost)
        score_mean = np.mean(scores)
        score_std = np.std(scores)
        W_N_mean = np.mean(W_Ns)
        W_N_std = np.std(W_Ns)
        l_mean = np.mean(l_costs)
        l_std = np.std(l_costs)
        m_mean = np.mean(m_costs)
        m_std = np.std(m_costs)
        # print('score:', score_mean, '±', score_std)
        # print('W/N:', W_N_mean, '±', W_N_std)
        return score_mean, score_std, W_N_mean, W_N_std, l_mean, l_std, m_mean, m_std

    def run_one(self, in_filename, out_filename, in_param=None):
        out_f = open(out_filename, 'w')
        in_f = open(in_filename, 'r')
        L, N, S = [int(v) for v in in_f.readline().split(' ')]
        if in_param is not None:
            assert L == in_param[0]
            assert N == in_param[1]
            assert S == in_param[2]
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

        judge = MockJudge(A, f, landing_pos, out_f, L, display=False)
        solver = Solver2(L, N, S, landing_pos, judge, display=False)
        solver.solve()
        out_f.close()
        return judge.evaluate()
        


if __name__ == '__main__':
    unittest.main()
