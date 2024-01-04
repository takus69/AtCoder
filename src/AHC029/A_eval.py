from dataclasses import dataclass
from enum import Enum
import sys

MAX_INVEST_LEVEL = 20


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
        self.next_cards = None

    def solve(self) -> int:
        self.turn = 0
        self.money = 0
        self.invest_level = 0
        self.cards = self.judge.read_initial_cards()
        self.projects = self.judge.read_projects()

        for _ in range(self.t):
            self._play(self.judge)
        # 最後のカードは無償を選択
        self.judge.select_card(0)

        return self.money

    def _play(self, judge):
        self.turn += 1
        # 行動の決定
        select_card_i, use_card_i, use_target = self._select_action()
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

    def _select_action(self) -> tuple[int, int, int]:
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
            self.money -= self.next_cards[select_card_i].p

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
