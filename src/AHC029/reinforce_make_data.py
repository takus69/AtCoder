from test_reinforce import run
import numpy as np
from tqdm import tqdm
import pandas as pd


def make_data(input_df=None, output_df=None):
    data = {'i': [], 'score': []}
    if input_df is None:
        input_dfs = []
        output_dfs = []
    else:
        input_dfs = [input_df]
        output_dfs = [output_df]
    for i in tqdm(range(50)):
        score = run(i)
        data['i'].append(i)
        data['score'].append(score)
        # 学習データの作成
        input_dfs.append(pd.read_csv('input.csv'))
        output_dfs.append(pd.read_csv('output.csv'))
    train_df = pd.concat(input_dfs, axis=0)
    target_df = pd.concat(output_dfs, axis=0)
    train_df.to_csv('train.csv', index=False)
    target_df.to_csv('target.csv', index=False)
    print('学習データ作成: train:', len(train_df), ', target:', len(target_df))

    print('score', format(np.sum(data['score']), ','))
    pd.DataFrame(data).to_csv('result.csv', index=False)
    return train_df, target_df


if __name__ == '__main__':
    make_data()
