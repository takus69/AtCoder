from test_A import run
import numpy as np
from tqdm import tqdm
import pandas as pd


data = {'i': [], 'N': [], 'M': [], 'e': [], 'cost': [], 'score': []}
scores = []
for i in tqdm(range(50)):
    r = run(i)
    data['i'].append(i)
    data['N'].append(r['N'])
    data['M'].append(r['M'])
    data['e'].append(r['e'])
    data['cost'].append(r['cost'])
    data['score'].append(r['score'])
print('score', format(np.sum(data['score']), ','))
pd.DataFrame(data).to_csv('result.csv', index=False)
