from test_A import run
import numpy as np
from tqdm import tqdm
import pandas as pd
import time
import multiprocessing


def main(i):
    start = time.time()
    r = run(i)
    t = round(time.time()-start, 4)
    N = r['N']
    M = r['M']
    e = r['e']
    cost = r['cost']
    score = r['score']
    data = [i, N, M, e, cost, score, t]
    print('\r', 'end', i, end='')
    return data


if __name__ == '__main__':
    trial = 100
    processes = multiprocessing.cpu_count()
    result = []
    with multiprocessing.Pool(processes=processes) as pool:
        data = [pool.apply_async(main, (i,)) for i in range(trial)]
        result = [d.get() for d in data]
    print()
    df = pd.DataFrame(result, columns=['i', 'N', 'M', 'e', 'cost', 'score', 'time'])
    df.to_csv('result.csv', index=False)
    print('score', format(int(df['score'].sum()*50/trial), ','))
