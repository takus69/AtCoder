from test_A import run
import numpy as np
from tqdm import tqdm
import pandas as pd


data = {'i': [], 'score': []}
scores = []
for i in tqdm(range(50)):
    score = run(i)
    data['i'].append(i)
    data['score'].append(score)
    if score == 0:
        print(f'{i} score is 0')
print('score', format(np.sum(data['score']), ','))
pd.DataFrame(data).to_csv('result.csv', index=False)
