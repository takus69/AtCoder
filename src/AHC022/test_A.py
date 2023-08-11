import unittest
from typing import List
from A import Pos, Judge, Solver
'''
ToDo
- 生成inputによるシミュレーション(Done)
- output生成(ビジュアライザーに入力可能)(Done)
- ファイル入出力
- 評価関数
'''

class MockJudge(Judge):
    def __init__(self, A, f, landing_pos):
        self.A = A
        self.f = f
        self.cnt = 0
        self.landing_pos = landing_pos

    def set_temperature(self, temperature: List[List[int]]) -> None:
        super().set_temperature(temperature)
        self.temperature = temperature

    def measure(self, i, y, x):
        print(f"{i} {y} {x}", flush=True)
        a = self.A[i]
        pos = self.landing_pos[a]
        r = pos.y + y
        c = pos.x + x
        return self.temperature[r][c] + self.f[self.cnt]
        

class TestA(unittest.TestCase):
    def test_simulator(self):
        L, N, S = [int(v) for v in input().split(" ")]
        landing_pos = []
        for _ in range(N):
            y, x = (int(v) for v in input().split(" "))
            landing_pos.append(Pos(y, x))
        A = []
        for _ in range(N):
            A.append(int(input()))
        f = []
        for _ in range(10000):
            f.append(int(input()))


        solver = Solver(L, N, S, landing_pos, MockJudge(A, f, landing_pos))
        solver.solve()


if __name__ == '__main__':
    unittest.main()
