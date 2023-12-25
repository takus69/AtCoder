from test_reinforce import run
import numpy as np
from tqdm import tqdm
import pandas as pd
import random


SAMPLE_CNT = 50

def make_data(input_df=None, output_df=None):
    data = {'i': [], 'score': []}
    if input_df is None:
        input_dfs = []
        output_dfs = []
    else:
        input_dfs = [input_df]
        output_dfs = [output_df]
    for i in tqdm(range(SAMPLE_CNT)):
        score = run(i)
        data['i'].append(i)
        data['score'].append(score)
        # 学習データの作成
        input_dfs.append(pd.read_csv('input.csv'))
        output_dfs.append(pd.read_csv('output.csv'))
    train_df = pd.concat(input_dfs, axis=0)
    target_df = pd.concat(output_dfs, axis=0)
    # 10エピソード分だけランダムで残す(SAMPLE_CNT * 1000 * 10)
    MAX_CNT = SAMPLE_CNT*1000*10
    if len(train_df) > MAX_CNT:
        sample_index = random.sample(range(len(train_df)), k=MAX_CNT)
        train_df, target_df = train_df.iloc[sample_index], target_df.iloc[sample_index]
    train_df.to_csv('train.csv', index=False)
    target_df.to_csv('target.csv', index=False)
    print('学習データ作成: train:', len(train_df), ', target:', len(target_df))

    print('score', format(np.sum(data['score']), ','))
    pd.DataFrame(data).to_csv('result.csv', index=False)
    return train_df, target_df, np.sum(data['score'])


if __name__ == '__main__':
    make_data()
