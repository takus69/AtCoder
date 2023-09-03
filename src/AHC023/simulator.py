from A import Solver
import os
import numpy as np
from tqdm import tqdm


def run(in_file, out_file):
    solver = Solver()
    solver.set_filepath(in_file, out_file)
    solver.read_input()
    solver.make_plan()
    solver.submission()
    return solver.evaluate()


def run_seed(folder_name):
    print(folder_name)
    filepath = 'testcases/{}'.format(folder_name)
    scores = []
    for i in tqdm(range(100)):
        in_filename = os.path.join(filepath, '{:04}.txt'.format(i))
        out_filename = os.path.join(filepath, '{:04}_out.txt'.format(i))
        score = run(in_filename, out_filename)
        scores.append(score)
    print('{} ± {}'.format(np.mean(scores), np.std(scores)))


if __name__ == '__main__':
    run_seed('seed0')
    run_seed('seed1')
    run_seed('seed2')
    run_seed('seed3')
