from test_A import MockSolver
from tqdm import tqdm
import os
import numpy as np
import pandas as pd
import time


def run(in_file, out_file):
    solver = MockSolver(in_file, out_file)
    score = solver.solve()
    return score, solver.N, np.mean(solver.d), solver.trial_cnt, solver.go_cnt, solver.short_cnt


if __name__ == '__main__':
    filepath = 'testcases'
    scores = []
    data = {'N': [], 'd': [], 'time': [], 'trial_cnt': [], 'go_cnt': [], 'short_cnt': []}
    for i in tqdm(range(100)):
        start = time.time()
        in_file = os.path.join(filepath, '{:04}.txt'.format(i))
        out_file = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score, N, d, trial_cnt, go_cnt, short_cnt = run(in_file, out_file)
        scores.append(score)
        data['N'].append(N)
        data['d'].append(d)
        data['time'].append(time.time()-start)
        data['trial_cnt'].append(trial_cnt)
        data['go_cnt'].append(go_cnt)
        data['short_cnt'].append(short_cnt)
    print('スコア平均: {} ± {}'.format(format(round(np.mean(scores)), ','), format(round(np.std(scores)), ',')))
    print('スコア: {}'.format(format(round(np.mean(scores)*50), ',')))
    data['score'] = scores
    pd.DataFrame(data).to_csv('result.csv')
