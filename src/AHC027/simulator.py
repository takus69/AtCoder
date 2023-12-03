from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np
import pandas as pd


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    score = solver.solve()
    return score


if __name__ == '__main__':
    filepath = 'testcases'
    scores = []
    for i in tqdm(range(100)):
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score = run(in_file, out_file)
        scores.append(score)
        # estimate_scores.append(estimate_score)
    print('スコア平均: {} ± {}'.format(format(round(np.mean(scores)), ','), format(round(np.std(scores)), ',')))
    print('スコア: {}'.format(format(round(np.mean(scores)*50), ',')))
    pd.DataFrame({'score': scores}).to_csv('result.csv')
