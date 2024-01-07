from dataclasses import dataclass
from enum import Enum
import random
from random import randint, gauss

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
        cards = [Card(CardType(0), 2**self.L, 0)]
        for _ in range(self.k-1):
            cards.append(self.create_card())
        return cards

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
        self.next_cards = None
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.pre_use_card_i = None

    def solve(self) -> int:
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_projects()

        for _ in range(self.t):
            actions = self._select_action()
            money = self._simulate(actions)
            self.money = self._play(self.judge, actions)
            self.judge.comment(f'actions: select card: {actions[0]}, use card: {actions[1]}, project: {actions[2]}')
            self.judge.comment(f'turn: {self.turn}, simulate money: {money}, momney: {self.money}')
            assert money == self.money
        # 最後のカードは無償を選択
        self.judge.select_card(0)

        return self.money

    def _play(self, judge, actions):
        self.turn += 1
        # 行動の決定
        # select_card_i, use_card_i, use_target = self._select_action()
        select_card_i, use_card_i, use_target = actions
        self.judge.comment(f'turn: {self.turn}, (r, c, m)=({select_card_i}, {use_card_i}, {use_target})')

        # カードの選択
        if select_card_i >= 0:
            judge.select_card(select_card_i)

        # カード、プロジェクトの選択
        if self.cards[use_card_i].t == CardType.INVEST:
            self.invest_level += 1
        judge.use_card(use_card_i, use_target)

        self.projects = judge.read_projects()
        self.money = judge.read_money()
        self.next_cards = judge.read_next_cards()
        self.pre_use_card_i = use_card_i
        return self.money

    def _clone(self):
        judge = MockJudge(self.n, self.m, self.k, self.invest_level, self.turn, self.money)
        judge.projects = self.projects
        judge.cards = self.cards
        judge.next_cards = self.next_cards
        judge.pre_use_card_i = self.pre_use_card_i

        mock = Solver(self.n, self.m, self.k, self.t)
        mock.projects = self.projects
        mock.cards = self.cards
        mock.next_cards = self.next_cards
        mock.money = self.money
        mock.invest_level = self.invest_level
        mock.judge = judge
        mock.turn = self.turn
        mock.pre_use_card_i = self.pre_use_card_i
        return mock

    def _simulate(self, actions):
        mock = self._clone()
        self.judge.comment(f'clone money: {mock.money}')
        score = mock._play(mock.judge, actions)
        self.judge.comment(f'clone play money: {mock.money}')
        return score

    def _select_action(self) -> tuple[int, int, int]:
        '''
        score = 0
        actions = (0, 0, 0)
        for r in range(self.k):
            for c in range(self.n):
                for m in range(self.m):
                    tmp_score = self._simulate((r, c, m))
                    if tmp_score > score:
                        score = tmp_score
                        actions = (r, c, m)
        return actions
        '''
        # 補充するカードの選択
        if self.next_cards is not None:
            eval = 0
            select_card_i = 0
            for i in range(self.k):
                card = self.next_cards[i]
                if card.p <= self.money:
                    eval2 = self._eval_state(card)
                    self.judge.comment(f'{select_card_i}: {eval}, {i}: {eval2}')
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

    def _eval_state(self, r: Card):
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
