from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    solver.solve()
    score = solver.evaluate()
    return score


if __name__ == '__main__':
    filepath = 'testcases'
    scores = []
    for i in tqdm(range(100)):
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score = run(in_file, out_file)
        scores.append(score)
    print('{} ± {}'.format(format(np.mean(scores), ','), np.std(scores)))
    print('予測スコア: {}'.format(format(np.sum(scores), ',')))


