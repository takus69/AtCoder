import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
import pickle
from reinforce_make_data import make_data
import random


def make_network(hidden_layer_sizes=(32, 32,), iter=10, train=False, verbose=False):
    model = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, random_state=1, max_iter=iter, verbose=verbose)
    model.fit(X=np.zeros((1, 119)), y=np.zeros((1, 20)))
    return model

def train_one(model, train_df, target_df):
    model.fit(X=train_df, y=target_df)
    score = model.score(train_df, target_df)
    with open('coef.txt', 'wb') as f:
        pickle.dump(model.coefs_, f)
    with open('intercepts.txt', 'wb') as f:
        pickle.dump(model.intercepts_, f)
    return model, score

def load_param(model):
    with open('coef.txt', 'rb') as f:
        coefs = pickle.load(f)
    with open('intercepts.txt', 'rb') as f:
        intercepts = pickle.load(f)
    model.coefs_ = coefs
    model.intercepts_ = intercepts
    return model

if __name__ == '__main__':
    model = make_network(iter=100, train=True, verbose=False)
    train_df, target_df, score = make_data()
    r2s = []
    scores = [score]
    for i in range(100):
        print(f'{i+1}回目の学習')
        # sample_index = random.sample(range(len(train_df)), k=2000)
        # model, r2 = train_one(model, train_df.iloc[sample_index], target_df.iloc[sample_index])
        model, r2 = train_one(model, train_df, target_df)
        print(f'学習のR2値: {r2}')
        train_df, target_df, score = make_data(train_df, target_df)
        print(f'スコア: {score}')
        r2s.append(r2)
        scores.append(score)
        print('r2:', r2s)
        print('scores:', scores)
        if i % 10 == 0:
            with open(f'model_{i}.pkl', 'wb') as f:
                pickle.dump(model, f)
    '''
    kf = KFold()
    for train_index, test_index in (kf.split(train_df)):
        X_train = train_df.iloc[train_index]
        y_train = target_df.iloc[train_index]
        X_test = train_df.iloc[test_index]
        y_test = target_df.iloc[test_index]

        for i in range(50):
            model.fit(X=train_df, y=target_df)
            y_pred = model.predict(X_test)
            valid_r2 = r2_score(y_test, y_pred)
            print(f'{i}: valid R2: {valid_r2}')
    '''
