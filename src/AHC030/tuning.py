import numpy as np
from tqdm import tqdm
import pandas as pd
import time
import multiprocessing
import subprocess
import json
import optuna


def run(i, seed, d_rate, min_M):
    output_str = subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py {seed} {d_rate} {min_M} > out/{i:04}.txt', shell=True, capture_output=True, text=True).stderr
    result = json.loads(output_str.split('\n')[0].replace("'", '"'))
    return result

def main(i, seed, d_rate, min_M):
    start = time.time()
    r = run(i, seed, d_rate, min_M)
    t = round(time.time()-start, 4)
    N = r['N']
    M = r['M']
    e = r['e']
    d = r['d']
    cost = r['cost']
    score = r['score']
    data = [i, N, M, e, d, cost, score, t]
    return data

def run_all(d_rate=-1, min_M=20):
    scores = []
    for seed in tqdm(range(5)):
        trial = 200
        result = []
        processes = multiprocessing.cpu_count()
        with multiprocessing.Pool(processes=processes) as pool:
            data = [pool.apply_async(main, (i,seed,d_rate,min_M)) for i in range(trial)]
            result = [d.get() for d in data]
        df = pd.DataFrame(result, columns=['i', 'N', 'M', 'e', 'd', 'cost', 'score', 'time'])
        score = (df['cost']/df['M']).mean()
        scores.append(score)
    return np.mean(scores)

def objective(trial):
    d_rate = trial.suggest_int('d_rate', 1, 10)
    min_M = trial.suggest_int('min_M', 0, 20)
    score = run_all(d_rate=d_rate, min_M=min_M)
    return score


if __name__ == '__main__':
    study_name = 'tuning_v16'
    study = optuna.create_study(
        study_name=study_name,
        storage=f'sqlite:///{study_name}.db',
        load_if_exists=True)
    study.optimize(objective, n_trials=100)
