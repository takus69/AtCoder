from dataclasses import dataclass
from enum import IntEnum
import sys
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
import warnings
from reinforce_train import make_network, load_param

warnings.simplefilter('ignore')

MAX_INVEST_LEVEL = 20
MAX_T = 1000
MAX_N = 7
MAX_M = 8
MAX_K = 5
gamma = 0.99


@dataclass
class Project:
    h: int
    v: int


class CardType(IntEnum):
    WORK_SINGLE = 0
    WORK_ALL = 1
    CANCEL_SINGLE = 2
    CANCEL_ALL = 3
    INVEST = 4


@dataclass
class Card:
    t: CardType
    w: int
    p: int


class Judge:

    def __init__(self, n: int, m: int, k: int):
        self.n = n
        self.m = m
        self.k = k

    def read_initial_cards(self) -> list[Card]:
        cards = []
        for _ in range(self.n):
            t, w = map(int, input().split())
            cards.append(Card(CardType(t), w, 0))
        return cards

    def read_projects(self) -> list[Project]:
        projects = []
        for _ in range(self.m):
            h, v = map(int, input().split())
            projects.append(Project(h, v))
        return projects

    def use_card(self, c: int, m: int) -> None:
        print(f"{c} {m}", flush=True)

    def read_money(self) -> int:
        return int(input())

    def read_next_cards(self) -> list[Card]:
        cards = []
        for _ in range(self.k):
            t, w, p = map(int, input().split())
            cards.append(Card(CardType(t), w, p))
        return cards

    def select_card(self, r: int) -> None:
        print(r, flush=True)

    def comment(self, message: str) -> None:
        print(f"# {message}")


class Solver:

    def __init__(self, n: int, m: int, k: int, t: int):
        self.n = n
        self.m = m
        self.k = k
        self.t = t
        self.judge = Judge(n, m, k)
        self.k_map = {0: []}
        self.input_datas = []
        self.output_datas = []
        self.model = make_network()
        self.model = load_param(self.model)

    def solve(self) -> int:
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_projects()

        # 学習データの初期値
        input_data = self.make_input_data([])
        self.judge.comment(f'learning data: {input_data}')
        self.input_datas.append(input_data)
        # r, c, m(c, mは次のターン内で登録)
        output_data = [0]

        for _ in range(self.t):
            self.predict(input_data)
            use_card_i, use_target = self._select_action()
            if self.cards[use_card_i].t == CardType.INVEST:
                self.invest_level += 1
            # example for comments
            self.judge.use_card(use_card_i, use_target)
            assert self.invest_level <= MAX_INVEST_LEVEL

            self.projects = self.judge.read_projects()
            self.money = self.judge.read_money()

            next_cards = self.judge.read_next_cards()
            select_card_i = self._select_next_card(next_cards)
            self.cards[use_card_i] = next_cards[select_card_i]
            self.judge.select_card(select_card_i)
            self.money -= next_cards[select_card_i].p
            assert self.money >= 0

            self.turn += 1

            # 学習データ出力
            input_data = self.make_input_data(next_cards)
            self.judge.comment(f'learning data: {input_data}')
            self.input_datas.append(input_data)
            output_data += [use_card_i, use_target]
            self.output_datas.append(output_data)
            # 次のターン用のoutput_data
            output_data = [select_card_i]

        return self.money
    
    def make_input_data(self, next_cards):
        data = [self.k, self.n, self.m, self.turn, self.money, self.invest_level]
        # 補充できる方針カード
        for i in range(MAX_K):
            if i < len(next_cards):
                # 有無,t,w,p
                # print(int(self.cards[i].t), file=sys.stderr)
                data += [1] + list(np.eye(5)[int(next_cards[i].t)]) + [next_cards[i].w, next_cards[i].p]
            else:
                data += [0]*8
        # 使用できる方針カード
        for i in range(MAX_N):
            if i < self.n:
                # 有無,t,w
                data += [1] + list(np.eye(5)[int(self.cards[i].t)]) + [self.cards[i].w]
            else:
                data += [0]*7
        # 選択できるプロジェクト
        for i in range(MAX_M):
            if i < self.m:
                # 有無,h,v
                data += [1, self.projects[i].h, self.projects[i].v]
            else:
                data += [0]*3
        return data


    def _select_action(self) -> tuple[int, int]:
        # 使用する方針カードの選択
        pred_c = self.pred[MAX_K:MAX_K+MAX_N]
        card_i = -1
        max_pred = -1
        for i in range(self.n):
            if max_pred < pred_c[i]:
                card_i = i
                max_pred = pred_c[i]

        # プロジェクトの選択
        if self.cards[card_i].t in [CardType.WORK_SINGLE, CardType.CANCEL_SINGLE]:
            pred_m = self.pred[MAX_K+MAX_N:MAX_K+MAX_N+MAX_M]
            project_i = -1
            max_pred = -1
            for i in range(self.m):
                if max_pred < pred_m[i]:
                    project_i = i
                    max_pred = pred_m[i]
        else:
            project_i = 0
        return (card_i, project_i)

    def _select_next_card(self, next_cards: list[Card]) -> int:
        pred_r = self.pred[:MAX_K]
        select_i = -1
        max_pred = -1
        for i in range(self.k):
            card = next_cards[i]
            if card.p <= self.money:
                if max_pred < pred_r[i]:
                    select_i = i
                    max_pred = pred_r[i]
        return select_i

    def predict(self, input_data):
        self.pred = self.model.predict(np.array(input_data).reshape(1, -1))[0]
        self.pred -= np.min(self.pred)

def make_learning_data(input_datas, output_datas):
    input_df = pd.DataFrame(input_datas)
    r_diff = np.diff(input_df.iloc[:, 4])
    # 報酬の算出
    rewards = [(MAX_T-1, r_diff[MAX_T-1])]
    pre_reward = r_diff[MAX_T-1]
    for i in range(MAX_T-2, -1, -1):
        reward = r_diff[i]+gamma*pre_reward
        rewards.append((i, reward))
        pre_reward = reward
    rewards = sorted(rewards, key=lambda x: x[0])
    # print(rewards, file=sys.stderr)
    # input_dfの最後の行(MAX_Tの行)は、アクションしていないため削除
    input_df = input_df.iloc[0:MAX_T]
    # output_df
    outputs = []
    for i in range(MAX_T):
        r, c, m = output_datas[i]
        reward = rewards[i][1]
        data = [0]*(MAX_K+MAX_N+MAX_M)
        data[r] = reward
        data[MAX_K+c] = reward
        data[MAX_K+MAX_N+m] = reward
        outputs.append(data)
    output_df = pd.DataFrame(outputs)
    return input_df, output_df


def main():
    n, m, k, t = map(int, input().split())
    solver = Solver(n, m, k, t)
    solver.solve()
    input_df, output_df = make_learning_data(solver.input_datas, solver.output_datas)
    input_df.to_csv('input.csv', index=False)
    output_df.to_csv('output.csv', index=False)
    # print('input:', len(input_df), ', output:', len(output_df), file=sys.stderr)
    


if __name__ == "__main__":
    main()
