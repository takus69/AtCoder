import unittest
from typing import List
import math
from A import Pos, Judge, Solver
'''
ToDo
- 生成inputによるシミュレーション(Done)
- output生成(ビジュアライザーに入力可能)(Done)
- ファイル入出力(Done)
- 評価関数(Done)
'''

class MockJudge(Judge):
    def __init__(self, A, f, landing_pos, out_f):
        self.A = A
        self.f = f
        self.cnt = 0
        self.landing_pos = landing_pos
        self.out_f = out_f
        self.landing_cost = 0
        self.measure_cost = 0

    def set_temperature(self, temperature: List[List[int]]) -> None:
        super().set_temperature(temperature)
        self.temperature = temperature
        for row in temperature:
            self.out_f.write(' '.join(map(str, row))+'\n')
        L = len(temperature)
        for i in range(L):
            for j in range(L):
                self.landing_cost += (temperature[i][j] - temperature[(i+1)%L][j])**2 + (temperature[i][j] - temperature[i][(j+1)%L])**2

    def measure(self, i, y, x):
        print(f'{i} {y} {x}', flush=True)
        self.out_f.write(f'{i} {y} {x}\n')
        a = self.A[i]
        pos = self.landing_pos[a]
        r = pos.y + y
        c = pos.x + x
        v = self.temperature[r][c] + self.f[self.cnt]
        self.out_f.write(f'# measure i={i} y={y} x={x}, value={v}\n')
        self.measure_cost += 100 * (10 + abs(y) + abs(x))
        self.cnt += 1
        return v
    
    def answer(self, estimate: List[int]) -> None:
        super().answer(estimate)
        self.out_f.write('-1 -1 -1\n')
        for e in estimate:
            self.out_f.write(str(e)+'\n')
        self.estimate = estimate

    def evaluate(self):
        print(f'配置コスト: {self.landing_cost}')
        print(f'計測時コスト: {self.measure_cost}')
        N = len(self.A)
        W = 0
        for i in range(N):
            if self.A[i] != self.estimate[i]:
                W += 1
        print(f'誤り数: {W}/{N}')
        score = math.ceil((10**14 * (0.8**W)) / (self.landing_cost + self.measure_cost + 10**5))
        print(f'得点: {score}')
        

class TestA(unittest.TestCase):
    def test_simulator(self):
        out_f = open('output.txt', 'w')
        in_f = open('input.txt', 'r')
        L, N, S = [int(v) for v in in_f.readline().split(' ')]
        landing_pos = []
        for _ in range(N):
            y, x = (int(v) for v in in_f.readline().split(' '))
            landing_pos.append(Pos(y, x))
        A = []
        for _ in range(N):
            A.append(int(in_f.readline()))
        f = []
        for _ in range(10000):
            f.append(int(in_f.readline()))
        in_f.close()

        judge = MockJudge(A, f, landing_pos, out_f)
        solver = Solver(L, N, S, landing_pos, judge)
        solver.solve()
        out_f.close()
        judge.evaluate()


if __name__ == '__main__':
    unittest.main()
