from typing import List
import sys
import queue


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Judge:
    def __init__(self, display=True):
        self.display = display

    def set_temperature(self, temperature: List[List[int]]) -> None:
        for row in temperature:
            if self.display:
                print(' '.join(map(str, row)))
        sys.stdout.flush()

    def measure(self, i: int, y: int, x: int) -> int:
        if self.display:
            print(f'{i} {y} {x}', flush=True)
        v = int(input())
        if v == -1:
            print(f'something went wrong. i={i} y={y} x={x}', file=sys.stderr)
            sys.exit(1)
        return v

    def answer(self, estimate: List[int]) -> None:
        if self.display:
            print('-1 -1 -1')
        for e in estimate:
            if self.display:
                print(e)
        sys.stdout.flush()


class Solver:

    def __init__(self, L: int, N: int, S: int, landing_pos: List[Pos], judge, display=True):
        '''
        10 <= L <= 50
        60 <= N <= 100
        1 <= S <= 90(i**2, 1 <= i <= 30)
        0 <= P <= 1000
        '''
        self.L = L
        self.N = N
        self.S = S
        self.landing_pos = landing_pos
        self.judge = judge
        self.display = display

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)

    def _create_temperature(self) -> List[List[int]]:
        dic_r = {r:[] for r in range(self.L)}
        self.dic_pos = {}
        min_r, max_r = self.L, 0
        for i, pos in enumerate(self.landing_pos):
            r = self._cal_radius(pos.y, pos.x)
            dic_r[r].append((pos.y, pos.x))
            self.dic_pos[(pos.y, pos.x)] = {'i': i, 'r': r, 't': -1}
            min_r = min(min_r, r)
            max_r = max(max_r, r)
        temp = 1000
        for r in range(self.L):
            for pos in dic_r[r]:
                self.dic_pos[pos]['t'] = temp
                temp -= 10
        r_poses = self._get_r_poses()
        r_temps = []
        for r in range(self.L):
            if len(dic_r[r]) > 0:
                temp = 0
                for pos in dic_r[r]:
                    temp += self.dic_pos[pos]['t']
                temp //= len(dic_r[r])
                r_temps.append((r, temp))
        r_temps.append((self.L-1, r_temps[-1][1]))
        temperature = [[-1]*self.L for _ in range(self.L)]
        pre_r, pre_temp = -1, r_temps[0][1]
        for r, temp in r_temps:
            if r != pre_r:
                diff = (pre_temp - temp) // (r - pre_r)
            else:
                diff = 0
            for rr in range(pre_r+1, r+1):
                for pos in r_poses[rr]:
                    temperature[pos.y][pos.x] = int(pre_temp - diff * (rr - pre_r))
            pre_r, pre_temp = r, temp
        for pos, v in self.dic_pos.items():
            temperature[pos[0]][pos[1]] = int(v['t'])
        return temperature

    def _predict(self, temperature: List[List[int]]) -> List[int]:
        estimate = [-1] * self.N
        for i_in in range(self.N):

            measured_value = 0
            retry_cnt = min(100, self.S*10)
            for _ in range(retry_cnt):
                measured_value += self.judge.measure(i_in, 0, 0)
            measured_value /= retry_cnt
            if self.display:
                print(f'# measure i={i_in} y=0 x=0, value={measured_value}')
            # answer the position with the temperature closest to the measured value
            min_diff = 9999
            for i_out, pos in enumerate(self.landing_pos):
                diff = abs(temperature[pos.y][pos.x] - measured_value)
                if diff < min_diff:
                    min_diff = diff
                    estimate[i_in] = i_out
        return estimate
    
    def _cal_radius(self, y, x):
        center_y = (self.L-1)/2
        center_x = (self.L-1)/2
        r = int(abs(x - center_x) + abs(y - center_y))
        return r
    
    def _get_r_poses(self):
        r_poses = {r:[] for r in range(self.L)}
        for i in range(self.L):
            for j in range(self.L):
                r = self._cal_radius(i, j)
                r_poses[r].append(Pos(i, j))
        return r_poses


def main():
    L, N, S = [int(v) for v in input().split(' ')]
    landing_pos = []
    for _ in range(N):
        y, x = (int(v) for v in input().split(' '))
        landing_pos.append(Pos(y, x))

    solver = Solver(L, N, S, landing_pos, Judge())
    solver.solve()


if __name__ == '__main__':
    main()