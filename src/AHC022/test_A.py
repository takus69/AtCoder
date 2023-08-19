import unittest
from typing import List
import math
from A import Pos, Judge, Solver, Solver2
'''
ToDo
- 生成inputによるシミュレーション(Done)
- output生成(ビジュアライザーに入力可能)(Done)
- ファイル入出力(Done)
- 評価関数(Done)
- 配置の最適化(徐々に変化)(Done)
- 標準出力ON/OFF機能(Done)
- L: 10, 25, 50 N: 60, 80, 100 S: 1, 9, 25, 49, 81, 400, 900の3*3*7=63パターンの結果評価(Done)
- 相対位置による場所の推定方法(Done)
- 近い距離から処理(Done)
- すでに分かっている対象は測定除外する(Done)
- SolverとSolver2の比較処理(Done)
- 計測コストの最適化(連続測定で、測定回数削減)⇒測定回数をSの値により最適化(Done)
  - S*S/40000(得点はあがったものの、順位表は下がった)(Done)
  - S/100(シミュレーションの得点はほぼ変わらず)(順位が上がったためこちらを採用)(Done)
- 基準からの測定でコストが少ない方を選択する(Done)
- 基準の位置最適化(中心近くがいい？)(Done)
- S=900の対策(retry回数を変更)
- 配置コストの最適化(Sが小さいものは1000でなくてもいい)
'''

class MockJudge(Judge):
    def __init__(self, A, f, landing_pos, out_f, L, display=True):
        self.A = A
        self.f = f
        self.L = L
        self.cnt = 0
        self.landing_pos = landing_pos
        self.out_f = out_f
        self.landing_cost = 0
        self.measure_cost = 0
        self.display = display

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
        if self.display:
            print(f'{i} {y} {x}', flush=True)
        self.out_f.write(f'{i} {y} {x}\n')
        a = self.A[i]
        pos = self.landing_pos[a]
        r = (pos.y + y)%self.L
        c = (pos.x + x)%self.L
        v = max(0, min(1000, self.temperature[r][c] + self.f[self.cnt]))
        self.cnt += 1
        self.out_f.write(f'# {self.cnt}: measure i={i} y={y} x={x}, value={v}\n')
        self.measure_cost += 100 * (10 + abs(y) + abs(x))
        return v

    def measure_n(self, i, y, x, retry_cnt):
        measured_value = super().measure_n(i, y, x, retry_cnt)
        if self.display:
            print(f'# measure_n i={i} y={y} x={x}, retry_cnt={retry_cnt}, value={measured_value}')
        self.out_f.write(f'# measure_n i={i} y={y} x={x}, retry_cnt={retry_cnt}, value={measured_value}\n')
        return measured_value
    
    def answer(self, estimate: List[int]) -> None:
        super().answer(estimate)
        self.out_f.write('-1 -1 -1\n')
        for e in estimate:
            self.out_f.write(str(e)+'\n')
        self.estimate = estimate

    def evaluate(self):
        '''
        0 <= 配置コスト <= 10^6*50*50*2=5*10^9
        10^3 <= 計測時コスト(1回あたり) <= 1.1*10^4
        10^7 <= 計測時コスト(全測定) <= 1.1*10^8
        '''
        N = len(self.A)
        W = 0
        for i in range(N):
            if self.A[i] != self.estimate[i]:
                W += 1
        score = math.ceil((10**14 * (0.8**W)) / (self.landing_cost + self.measure_cost + 10**5))
        if self.display:
            print(f'配置コスト: {self.landing_cost}')
            print(f'計測時コスト: {self.measure_cost}')
            print(f'誤り数: {W}/{N}')
            print(f'得点: {score}')
        return score, W, N, self.landing_cost, self.measure_cost
        

class TestA(unittest.TestCase):
    def test_simulator(self):
        out_f = open('output900.txt', 'w')
        in_f = open('input900.txt', 'r')
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

        judge = MockJudge(A, f, landing_pos, out_f, L)
        solver = Solver2(L, N, S, landing_pos, judge)
        solver.solve()
        out_f.close()
        judge.evaluate()

    def test_create_temperature(self):
        landing_pos = []
        landing_pos.append(Pos(1, 1))
        landing_pos.append(Pos(5, 5))
        landing_pos.append(Pos(2, 3))
        solver = Solver(10, 3, 1, landing_pos, MockJudge([], [], [], None, 10))
        print(solver._create_temperature())

        landing_pos = []
        landing_pos.append(Pos(4, 4))
        landing_pos.append(Pos(5, 5))
        landing_pos.append(Pos(4, 5))
        landing_pos.append(Pos(2, 3))
        landing_pos.append(Pos(5, 8))
        solver = Solver(10, 5, 1, landing_pos, MockJudge([], [], [], None, 10))
        for t in solver._create_temperature():
            print(t)

    def test_solver(self):
        # L=1
        solver = Solver(1, 0, 0, [], MockJudge([], [], [], None, 1))
        r_posses = solver._get_r_poses()
        self.assertEqual(len(r_posses), 1)
        poses = r_posses[0]
        self.assertEqual(len(poses), 1)
        self.assertEqual(poses[0].y, 0)
        self.assertEqual(poses[0].x, 0)

        # L=2
        solver = Solver(2, 0, 0, [], MockJudge([], [], [], None, 2))
        r_posses = solver._get_r_poses()
        self.assertEqual(len(r_posses), 2)
        poses = r_posses[0]
        self.assertEqual(len(poses), 0)
        poses = r_posses[1]
        self.assertEqual(len(poses), 4)
        l_poses = []
        for pos in poses:
            l_poses.append((pos.y, pos.x))
        l_poses = sorted(l_poses)
        pos = l_poses[0]
        self.assertEqual(pos[0], 0)
        self.assertEqual(pos[1], 0)
        pos = l_poses[1]
        self.assertEqual(pos[0], 0)
        self.assertEqual(pos[1], 1)
        pos = l_poses[2]
        self.assertEqual(pos[0], 1)
        self.assertEqual(pos[1], 0)
        pos = l_poses[3]
        self.assertEqual(pos[0], 1)
        self.assertEqual(pos[1], 1)

        # L=3
        solver = Solver(3, 0, 0, [], MockJudge([], [], [], None, 3))
        r_posses = solver._get_r_poses()
        self.assertEqual(len(r_posses), 3)
        poses = r_posses[0]
        self.assertEqual(len(poses), 1)
        poses = r_posses[1]
        self.assertEqual(len(poses), 4)
        l_poses = []
        for pos in poses:
            l_poses.append((pos.y, pos.x))
        l_poses = sorted(l_poses)
        pos = l_poses[0]
        self.assertEqual(pos[0], 0)
        self.assertEqual(pos[1], 1)
        pos = l_poses[1]
        self.assertEqual(pos[0], 1)
        self.assertEqual(pos[1], 0)
        pos = l_poses[2]
        self.assertEqual(pos[0], 1)
        self.assertEqual(pos[1], 2)
        pos = l_poses[3]
        self.assertEqual(pos[0], 2)
        self.assertEqual(pos[1], 1)
        poses = r_posses[2]
        self.assertEqual(len(poses), 4)
        l_poses = []
        for pos in poses:
            l_poses.append((pos.y, pos.x))
        l_poses = sorted(l_poses)
        pos = l_poses[0]
        self.assertEqual(pos[0], 0)
        self.assertEqual(pos[1], 0)
        pos = l_poses[1]
        self.assertEqual(pos[0], 0)
        self.assertEqual(pos[1], 2)
        pos = l_poses[2]
        self.assertEqual(pos[0], 2)
        self.assertEqual(pos[1], 0)
        pos = l_poses[3]
        self.assertEqual(pos[0], 2)
        self.assertEqual(pos[1], 2)

if __name__ == '__main__':
    unittest.main()
