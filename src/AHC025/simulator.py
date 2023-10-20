from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np
import pandas as pd


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    solver.solve()
    score = solver.evaluate()
    estimate_score = solver.estimate_score()
    if solver.q_cnt > solver.Q:
        print('クエリ回数オーバー: {}'.format(in_file))
    return solver.N, solver.D, solver.Q, score, estimate_score


if __name__ == '__main__':
    filepath = 'testcases'
    ret = {'N': [], 'D': [], 'Q': []}
    scores = []
    estimate_scores = []
    for i in tqdm(range(100)):
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        N, D, Q, score, estimate_score = run(in_file, out_file)
        scores.append(score)
        estimate_scores.append(estimate_score)
        ret['N'].append(N)
        ret['D'].append(D)
        ret['Q'].append(Q)
    print('実スコア: {} ± {}'.format(format(np.mean(scores), ','), np.std(scores)))
    print('予測スコア: {} ± {}'.format(format(np.mean(estimate_scores), ','), np.std(estimate_scores)))
    print('実スコア: {}'.format(format(np.sum(scores), ',')))
    print('予測スコア: {}'.format(format(np.sum(estimate_scores), ',')))
    ret['score'] = scores
    pd.DataFrame(ret).to_csv('result.csv')
