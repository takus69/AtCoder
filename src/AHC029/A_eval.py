from dataclasses import dataclass
from enum import Enum
import random
from random import randint, gauss
import sys

sys.setrecursionlimit(10**9)

MAX_INVEST_LEVEL = 20


def clamp(v, min_v, max_v):
    return max(min_v, min(v, max_v))

@dataclass
class Project:
    h: int
    v: int


class CardType(Enum):
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
        self.L = 0
        self.money = 0
        self.pre_use_card_i = -1

    def read_initial_cards(self) -> list[Card]:
        self.cards = []
        for _ in range(self.n):
            t, w = map(int, input().split())
            self.cards.append(Card(CardType(t), w, 0))
        return self.cards

    def read_projects(self) -> list[Project]:
        self.projects = []
        for _ in range(self.m):
            h, v = map(int, input().split())
            self.projects.append(Project(h, v))
        return self.projects

    def use_card(self, c: int, m: int, simulate=False) -> None:
        if not simulate:
            print(f"{c} {m}", flush=True)
        self.pre_use_card_i = c
        card = self.cards[c]
        if card.t == CardType.WORK_SINGLE:
            self.projects[m].h = max(self.projects[m].h-self.cards[c].w, 0)
            if self.projects[m].h == 0:
                self.money += self.projects[m].v
                self.projects[m] = None
        elif card.t == CardType.WORK_ALL:
            for i in range(self.m):
                self.projects[i].h = max(self.projects[i].h-self.cards[c].w, 0)
                if self.projects[i].h == 0:
                    self.money += self.projects[i].v
                    self.projects[i] = None
        elif card.t == CardType.INVEST:
            self.L += 1
            assert self.L <= MAX_INVEST_LEVEL
        elif card.t == CardType.CANCEL_SINGLE:
            self.projects[m] = None
        elif card.t == CardType.CANCEL_ALL:
            for i in range(self.m):
                self.projects[i] = None

    def read_money(self) -> int:
        self.money = int(input())
        return self.money

    def read_next_cards(self) -> list[Card]:
        self.next_cards = []
        for _ in range(self.k):
            t, w, p = map(int, input().split())
            self.next_cards.append(Card(CardType(t), w, p))
        return self.next_cards

    def select_card(self, r: int, simulate=False) -> None:
        if not simulate:
            print(r, flush=True)
        self.cards[self.pre_use_card_i] = self.next_cards[r]
        self.money -= self.next_cards[r].p

    def comment(self, message: str) -> None:
        print(f"# {message}")

    def eval_state(self) -> int:
        money = self.money
        pj_eval = 0
        pj_min_eval = (2**10)*(2*MAX_INVEST_LEVEL)
        for p in self.projects:
            if p is None:
                continue
            pj_eval += p.v - p.h
            pj_min_eval = min(pj_min_eval, p.v-p.h)
        card_eval = 0
        invest_flg = False
        for i in range(self.n):
            c = self.cards[i]
            if c is None:
                continue
            match c.t:
                case CardType.WORK_SINGLE:
                    card_eval += 0.9*c.w
                case CardType.WORK_ALL:
                    card_eval += 0.6*c.w * self.m
                case CardType.CANCEL_SINGLE:
                    card_eval += 2**self.L  #-pj_min_eval
                case CardType.CANCEL_ALL:
                    card_eval += 2**self.L  # -pj_eval
                case CardType.INVEST:
                    card_eval += 425*(2**self.L)
                    invest_flg = True
        next_card_eval = -(2**10)*(2*MAX_INVEST_LEVEL)
        for c in self.next_cards:
            if c.p > money:
                continue
            match c.t:
                case CardType.WORK_SINGLE:
                    tmp_eval = 0.9*c.w - c.p
                case CardType.WORK_ALL:
                    tmp_eval = 0.6*c.w*self.m - c.p
                case CardType.CANCEL_SINGLE:
                    tmp_eval = 2**self.L  # -pj_min_eval
                case CardType.CANCEL_ALL:
                    tmp_eval = 2**self.L  # -pj_eval
                case CardType.INVEST:
                    tmp_eval = 425*(2**self.L)
                    invest_flg = True
            next_card_eval = max(next_card_eval, tmp_eval)
        if invest_flg:
            pj_eval *= 2
            card_eval *= 2
            next_card_eval *= 2
        eval = money + pj_eval + card_eval + next_card_eval
        # self.judge.comment(f'{eval}: {self.money}, {self.t}, {self.turn}, {self.invest_level}, {money}, {pj_eval}, {card_eval}, {next_card_eval}')
        return eval


class MockJudge(Judge):
    def __init__(self, n: int, m: int, k: int, L: int, turn: int, money: int):
        self.n = n
        self.m = m
        self.k = k
        self.L = L
        self.turn = turn
        self.money = money
        self.set_x(randint(1, 20), randint(1, 10), randint(1, 10), randint(1, 5), randint(1, 3))

    def set_x(self, x0, x1, x2, x3, x4):
        self.x = [x0, x1, x2, x3, x4]
        sum_x = sum(self.x)
        pre_x = 0
        for i in range(len(self.x)):
            pre_x += self.x[i]
            self.x[i] = pre_x/sum_x

    def read_projects(self) -> list[Project]:
        for i in range(self.m):
            if self.projects[i] is None:
                self.projects[i] = self.create_project()
        return self.projects

    def create_project(self) -> Project:
        b = random.uniform(2, 8)
        h = round(2**b)*(2**self.L)
        v = round(2**clamp(gauss(b, 0.5), 0, 10))*(2**self.L)
        return Project(h, v)

    def read_next_cards(self) -> list[Card]:
        self.next_cards = [Card(CardType(0), 2**self.L, 0)]
        for _ in range(self.k-1):
            self.next_cards.append(self.create_card())
        return self.next_cards

    def create_card(self) -> Card:
        r = random.random()
        pre = 0
        for i in range(5):
            if pre <= r < self.x[i]:
                t = i
                break
            pre = self.x[i]
        if t == 0 or t == 1:
            w = randint(1, 50)*(2**self.L)
        else:
            w = 0
        if t == 0:
            w2 = w/(2**self.L)
            p = clamp(round(gauss(w2, w2/3)), 1, 10000)
        elif t == 1:
            w2 = self.m*w/(2**self.L)
            p = clamp(round(gauss(w2, w2/3)), 1, 10000)
        elif t == 2 or t == 3:
            p = randint(0, 10)*(2**self.L)
        elif t == 4:
            p = randint(200, 1000)*(2**self.L)
        return Card(CardType(t), w, p)

    def read_money(self) -> int:
        return self.money

    def use_card(self, c: int, m: int, simulate=False) -> None:
        super().use_card(c, m, True)

    def select_card(self, r: int, simulate=False) -> None:
        super().select_card(r, True)


class Solver:

    def __init__(self, n: int, m: int, k: int, t: int):
        self.n = n
        self.m = m
        self.k = k
        self.t = t
        self.judge = Judge(n, m, k)
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.pre_use_card_i = None
        self.next_cards = []
        self.cards = [None for _ in range(self.n)]
        self.projects = [None for _ in range(self.m)]
        self.eval_state = 0

    def set_card(self, i, card):
        self.cards[i] = card
        match card.t:
            case CardType.WORK_SINGLE:
                card_eval = 0.9*card.w
            case CardType.WORK_ALL:
                card_eval = 0.6*card.w * self.m
            case CardType.CANCEL_SINGLE:
                card_eval = 2**self.invest_level
            case CardType.CANCEL_ALL:
                card_eval = 2**self.invest_level
            case CardType.INVEST:
                card_eval = 425*(2**self.invest_level)
        self.eval_state += card_eval

    def set_project(self, i, project):
        self.projects[i] = project
        self.eval_state += project.v - project.h
    
    def work_project(self, c, m):
        self.judge.use_card(c, m)
        self.pre_use_card_i = c
        card = self.cards[c]
        if card.t == CardType.WORK_SINGLE:
            self.projects[m].h = max(self.projects[m].h-self.cards[c].w, 0)
            if self.projects[m].h == 0:
                self.money += self.projects[m].v
                self.projects[m] = None
        elif card.t == CardType.WORK_ALL:
            for i in range(self.m):
                self.projects[i].h = max(self.projects[i].h-self.cards[c].w, 0)
                if self.projects[i].h == 0:
                    self.money += self.projects[i].v
                    self.projects[i] = None
        elif card.t == CardType.INVEST:
            self.invest_level += 1
            assert self.L <= MAX_INVEST_LEVEL
        elif card.t == CardType.CANCEL_SINGLE:
            self.projects[m] = None
        elif card.t == CardType.CANCEL_ALL:
            for i in range(self.m):
                self.projects[i] = None
    
    def buy_card(self, r):
        None

    def solve(self) -> int:
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_projects()

        for _ in range(self.t):
            actions = self._select_action(True)
            self.judge.comment(f'turn: {self.turn}, (r, c, m)={actions}')
            # money = self._simulate(actions)
            score = self._play(self.judge, actions)
            self._read_state(self.judge)
            if actions[0] >= 0:
                select_card = self.next_cards[actions[0]]
            else:
                select_card = None
            self.judge.comment(f'play actions: {actions}, score: {score}, money: {self.money}, select_card: {select_card}, use_card: {self.cards[actions[1]]}, project: {self.projects[actions[2]]}')
            # self.judge.comment(f'actions: select card: {actions[0]}, use card: {actions[1]}, project: {actions[2]}')
            # self.judge.comment(f'turn: {self.turn}, simulate money: {money}, momney: {self.money}')
            # assert money == self.money
        # 最後のカードは無償を選択
        self.judge.select_card(0)

        return self.money

    def _play(self, judge, actions):
        # 行動の決定
        # select_card_i, use_card_i, use_target = self._select_action()
        select_card_i, use_card_i, use_target = actions

        # カードの選択
        if select_card_i >= 0:
            judge.select_card(select_card_i)
            self.turn += 1

        # カード、プロジェクトの選択
        if self.cards[use_card_i].t == CardType.INVEST:
            self.invest_level += 1
        judge.use_card(use_card_i, use_target)
        self.pre_use_card_i = use_card_i
        self.projects = judge.read_projects()
        self.money = judge.read_money()
        self.next_cards = judge.read_next_cards()
        return self.judge.eval_state()

    def _read_state(self, judge):
        return self.judge.eval_state()

    def _clone(self):
        judge = MockJudge(self.n, self.m, self.k, self.invest_level, self.turn, self.money)
        judge.projects = [Project(p.h, p.v) for p in self.projects]
        judge.cards = [c for c in self.cards]
        if len(self.next_cards) == 0:
            judge.next_cards = []
        else:
            judge.next_cards = [c for c in self.next_cards]
        judge.pre_use_card_i = self.pre_use_card_i

        mock = Solver(self.n, self.m, self.k, self.t)
        mock.projects = [p for p in self.projects]
        mock.cards = [c for c in self.cards]
        if len(self.next_cards) == 0:
            mock.next_cards = []
        else:
            mock.next_cards = [c for c in self.next_cards]
        mock.money = self.money
        mock.invest_level = self.invest_level
        mock.judge = judge
        mock.turn = self.turn
        mock.pre_use_card_i = self.pre_use_card_i
        return mock

    def _simulate(self, actions):
        mock = self._clone()
        score = mock._play(mock.judge, actions)
        # self.judge.comment(f'simulate actions: {actions}, money: {mock.money}, tmp score: {score}')
        # for _ in range(2):
            # actions, score = mock._play_all_actions(mock._play)
            # actions = mock._select_action(False)
            # self.judge.comment(f'simulute turn {mock.turn}: actions: {actions}, use_card: {mock.cards[actions[1]]}')
            # score = mock._play(mock.judge, actions)
        # self.judge.comment(f'simulate end: turn: {mock.turn}')
        return score

    def _play_all_actions(self, func):
        score = -1
        actions = (0, 0, 0)
        r_list = []
        if len(self.next_cards) == 0:
            r_list.append(-1)
        else:
            for i in range(self.k):
                if self.next_cards[i].p <= self.money:
                    r_list.append(i)
        for r in r_list:
            if r >= 0:
                self.cards[self.pre_use_card_i] = self.next_cards[r]
            for c in range(self.n):
                if self.cards[c].t in [CardType.CANCEL_SINGLE, CardType.WORK_SINGLE]:
                    m_list = range(self.m)
                else:
                    m_list = [0]
                for m in m_list:
                    # tmp_score = self._play(self.judge, (r, c, m))
                    mock = self._clone()
                    tmp_score = mock._play(mock.judge, actions)
                    # self.judge.comment(f'play all {self.turn}: actions: ({r}, {c}, {m}), score: {tmp_score}')
                    if tmp_score > score:
                        score = tmp_score
                        actions = (r, c, m)
                        # self.judge.comment(f'play all update {self.turn}: actions: {actions}, score: {score}')
        return actions, score

    def _select_action(self, simulate=False) -> tuple[int, int, int]:
        if simulate:
            score = -1
            actions = (0, 0, 0)
            r_list = []
            if len(self.next_cards) == 0:
                r_list.append(-1)
            else:
                for i in range(self.k):
                    if self.next_cards[i].p <= self.money:
                        r_list.append(i)
            for r in r_list:
                if r >= 0:
                    self.cards[self.pre_use_card_i] = self.next_cards[r]
                for c in range(self.n):
                    if self.cards[c].t in [CardType.CANCEL_SINGLE, CardType.WORK_SINGLE]:
                        m_list = range(self.m)
                    else:
                        m_list = [0]
                    for m in m_list:
                        # debug
                        if r >= 0:
                            select_card = self.next_cards[r]
                        else:
                            select_card = None
                        self.judge.comment(f'simulate start actions: ({r}, {c}, {m}), money: {self.money}, select_card: {select_card}, use_card: {self.cards[c]}, project: {self.projects[m]}')
                        tmp_score = 0
                        for _ in range(10):
                            tmp_score += self._simulate((r, c, m))
                        tmp_score //= 10
                        self.judge.comment(f'simulate actions: ({r}, {c}, {m}), money: {self.money}, tmp score: {tmp_score}')
                        if tmp_score > score:
                            score = tmp_score
                            actions = (r, c, m)
                            # self.judge.comment(f'simulate update score: {score}, actions: ({r}, {c}, {m}')
            return actions
        else:
            # 補充するカードの選択
            if len(self.next_cards) > 0:
                eval = 0
                select_card_i = 0
                for i in range(self.k):
                    card = self.next_cards[i]
                    if card.p <= self.money:
                        eval2 = self._eval_card(card)
                        if eval < eval2:
                            eval = eval2
                            select_card_i = i
            else:
                select_card_i = -1
            if select_card_i >= 0:
                self.cards[self.pre_use_card_i] = self.next_cards[select_card_i]

            # 使用するコードとプロジェクトの選択
            eval = 0
            use_card_i, use_target = 0, 0
            for c in range(self.n):
                for m in range(self.m):
                    eval2 = self._eval_action(c, m)
                    if eval < eval2:
                        use_card_i = c
                        use_target = m
                        eval = eval2
            if self.cards[use_card_i].t in [CardType.INVEST, CardType.WORK_ALL, CardType.CANCEL_ALL]:
                use_target = 0
            return (select_card_i, use_card_i, use_target)
    
    def _eval_action(self, c: int, m: int):
        card = self.cards[c]
        project = self.projects[m]
        eval = 0
        if card.t == CardType.WORK_SINGLE:
            eval = min(card.w, project.h)
        elif card.t == CardType.WORK_ALL:
            for p in self.projects:
                eval += min(card.w, p.h)
        return eval

    def _eval_card(self, r: Card):
        eval = 0
        if r.t == CardType.WORK_SINGLE:
            eval = r.w - r.p
        elif r.t == CardType.WORK_ALL:
            eval = r.w * self.m - r.p
        return self.money + eval


def main():
    n, m, k, t = map(int, input().split())
    solver = Solver(n, m, k, t)
    solver.solve()


if __name__ == "__main__":
    main()
