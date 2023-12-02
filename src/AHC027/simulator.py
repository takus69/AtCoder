from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np
import pandas as pd


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    solver.solve()
    score = solver.evaluate()
    solver.end()
    return score


if __name__ == '__main__':
    filepath = 'testcases'
    # ret = {'N': [], 'D': [], 'Q': []}
    scores = []
    # estimate_scores = []
    for i in tqdm(range(100)):
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score = run(in_file, out_file)
        scores.append(score)
        # estimate_scores.append(estimate_score)
    '''
    print('実スコア: {} ± {}'.format(format(np.mean(scores), ','), np.std(scores)))
    print('予測スコア: {} ± {}'.format(format(np.mean(estimate_scores), ','), np.std(estimate_scores)))
    print('実スコア: {}'.format(format(np.sum(scores), ',')))
    print('予測スコア: {}'.format(format(np.sum(estimate_scores), ',')))
    ret['score'] = scores
    pd.DataFrame(ret).to_csv('result.csv')
    '''
