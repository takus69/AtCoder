import unittest
from typing import List
from A import Pos, Judge, Solver
'''
ToDo
- 生成inputによるシミュレーション(Done)
- output生成(ビジュアライザーに入力可能)(Done)
- ファイル入出力(Done)
- 評価関数
'''

class MockJudge(Judge):
    def __init__(self, A, f, landing_pos, out_f):
        self.A = A
        self.f = f
        self.cnt = 0
        self.landing_pos = landing_pos
        self.out_f = out_f

    def set_temperature(self, temperature: List[List[int]]) -> None:
        super().set_temperature(temperature)
        self.temperature = temperature
        for row in temperature:
            self.out_f.write(' '.join(map(str, row))+'\n')

    def measure(self, i, y, x):
        print(f'{i} {y} {x}', flush=True)
        self.out_f.write(f'{i} {y} {x}\n')
        a = self.A[i]
        pos = self.landing_pos[a]
        r = pos.y + y
        c = pos.x + x
        v = self.temperature[r][c] + self.f[self.cnt]
        self.out_f.write(f'# measure i={i} y={y} x={x}, value={v}\n')
        return v
    
    def answer(self, estimate: List[int]) -> None:
        super().answer(estimate)
        self.out_f.write('-1 -1 -1\n')
        for e in estimate:
            self.out_f.write(str(e)+'\n')
        

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

        solver = Solver(L, N, S, landing_pos, MockJudge(A, f, landing_pos, out_f))
        solver.solve()
        out_f.close()


if __name__ == '__main__':
    unittest.main()
