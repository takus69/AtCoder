from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np
import pandas as pd


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    score = solver.solve()
    return score, solver.N, np.mean(solver.d)


if __name__ == '__main__':
    filepath = 'testcases'
    scores = []
    data = {'N': [], 'd': []}
    for i in tqdm(range(100)):
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score, N, d = run(in_file, out_file)
        scores.append(score)
        data['N'].append(N)
        data['d'].append(d)
    print('スコア平均: {} ± {}'.format(format(round(np.mean(scores)), ','), format(round(np.std(scores)), ',')))
    print('スコア: {}'.format(format(round(np.mean(scores)*50), ',')))
    data['score'] = scores
    pd.DataFrame(data).to_csv('result.csv')
