from dataclasses import dataclass
import sys
import numpy as np
import random
import itertools
import math


@dataclass
class Pos:
    i: int
    j: int


@dataclass
class Polyomino:
    d: int
    poses: list[Pos]


class Judge:

    def __init__(self):
        self.N, self.M, self.e = self._read_initial()
        self.oil_fields = []
        for _ in range(self.M):
            self.oil_fields.append(self._read_oil_field())
        self.cost = 0
    
    def read_initial(self) -> list[int, int, int]:
        return self.N, self.M, self.e

    def read_oil_fields(self) -> list[Polyomino]:
        return self.oil_fields

    def _read_initial(self) -> Polyomino:
        tmp = input().split()
        N, M, e = int(tmp[0]), int(tmp[1]), float(tmp[2])
        return N, M, e

    def _read_oil_field(self) -> Polyomino:
        dij = list(map(int, input().split()))
        d = dij[0]
        ij = dij[1:]
        poses = []
        for i in range(0, len(ij), 2):
            poses.append(Pos(ij[i], ij[i+1]))
        return Polyomino(d, poses)

    def query(self, poly: Polyomino) -> int:
        self.cost += 1/(poly.d**(1/2))
        s = f'q {poly.d}'
        for p in poly.poses:
            s += f' {p.i} {p.j}'
        print(s)
        return int(input())

    def answer(self, poses: list[Pos]) -> int:
        s = f'a {len(poses)}'
        for p in poses:
            s += f' {p.i} {p.j}'
        print(s)
        return int(input())

    def comment(self, message: str) -> None:
        print(f'# {message}')

    def std(self, *message: str) -> None:
        print(*message, file=sys.stderr)

    def color(self, p:  Pos, c: str) -> None:
        print(f'#c {p.i} {p.j} {c}')


class Solver:

    def __init__(self):
        self.judge = Judge()
        self.N, self.M, self.e = self.judge.read_initial()
        self.oil_fields = self.judge.read_oil_fields()
        self.oil_maps = []
        self.pattern_cnt = []
        self.mined = [[0]*self.N for _ in range(self.N)]
        self.ans = []
        self.v_map = [[2*self.M]*self.N for _ in range(self.N)]
        self.v_map2 = [[0]*self.N for _ in range(self.N)]

    def solve(self) -> dict:
        trial_cnt = 0
        sum_d = 0
        self.found_d = 0
        self.e_maps = []  # _expected_mapの結果を保持
        for poly in self.oil_fields:
            sum_d += poly.d
            self.e_maps.append(self._expected_map(poly))
        self.all_e_maps = self._merge_maps()
        self._show_map(self.pos_prob)
        # sorted_poses = self._sort_map(self.all_e_maps)
        sorted_poses = self._sort_map(self.pos_prob)
        while len(sorted_poses) > 0:
            trial_cnt += 1
            self.judge.std('trial cnt', trial_cnt)
            for i in range(len(sorted_poses)):
                e, pos = sorted_poses[i]
                if e == 1:
                    self.ans.append(pos)
                    self.mined[pos.i][pos.j] = 1
                    self.found_d += 1
                else:
                    break
            if e == 0:  # 初期の埋蔵量の期待値が0だと処理終了
                break
            e = self.all_e_maps[pos.i][pos.j]
            if e == 0 or self.mined[pos.i][pos.j]:  # 埋蔵量の期待値が0、もしくは、採掘済みはスキップ
                continue
            self.mined[pos.i][pos.j] = 1
            v = self._mining(pos)
            self.all_e_maps = self._update_e_maps_v(pos, v)
            self._show_map(self.pos_prob)
            self.found_d += v
            if self.found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
            sorted_poses = self._sort_map(self.pos_prob)
            '''
            self.v_map[pos.i][pos.j] = v - self.v_map2[pos.i][pos.j]
            if self.v_map[pos.i][pos.j] == 0:
                self.all_e_maps = self._update_e_maps(pos)
            self.found_d += v
            if self.found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
            sorted_poses = self._sort_map(self.all_e_maps)
            '''
        ret = self.judge.answer(self.ans)
        assert ret == 1
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, pos) -> int:
        v = self.judge.query(Polyomino(1, [pos]))
        self.judge.comment(f'query: (1, {pos}), v: {v}')
        if v > 0:
            self.ans.append(pos)
            # self.all_e_maps = self._update_e_maps_v(pos)
        '''
        else:
            # 埋蔵量の期待値を更新
            self.all_e_maps = self._update_e_maps(pos)
            self._show_map(self.all_e_maps)
        '''
        return v

    def _update_e_maps_v(self, pos, v):
        # self.judge.std(pos, v)
        # 各油田が位置posにある確率を算出
        p_pos_v = 0  # 位置posがvである確率
        p_pos_oils1 = [0 for _ in range(self.M)]  # 各油田が位置posにある確率
        p_pos_oils2 = [0 for _ in range(self.M)]  # 各油田が位置posにない確率
        for c in itertools.combinations(range(self.M), v):  # nCvの組み合わせを全て足し合わせる
            p = 1
            for i in range(self.M):
                if i in c:
                    p *= self.oil_maps[i][pos.i][pos.j]
                else:
                    p *= 1-self.oil_maps[i][pos.i][pos.j]
            p_pos_v += p
            for i in range(self.M):
                if i in c:
                    p_pos_oils1[i] += p
                else:
                    p_pos_oils2[i] += p

        # ベイズの定理で更新
        for i in range(self.M):
            ms = self.e_maps[i]
            pp = self.oil_maps[i][pos.i][pos.j]
            for j in range(len(ms)):
                m = ms[j][1]
                if (i == 0 and j == 50) or (i == 1 and j == 42):
                    self.judge.std(f'{i} pp={pp}, m={m[8][3]}, pos={pos}, v={v}, *={p_pos_oils1[i] / (pp * p_pos_v)}, p_pos_v={p_pos_v}, p_pos_oils1[i]={p_pos_oils1[i]}, p_pos_oils2[i]={p_pos_oils2[i]}')
                    self.judge.std(f'{[m[1].max() for m in ms]}')
                if v > 0:
                    if (pp == 0 and m[pos.i][pos.j] > 0) or (pp == 1 and m[pos.i][pos.j] == 0):
                        self.e_maps[i][j][1] = m * 0
                        self.e_maps[i][j][0] = False
                    else:
                        if m[pos.i][pos.j] > 0:
                            self.e_maps[i][j][1] = m * p_pos_oils1[i] / (pp * p_pos_v)
                        else:
                            self.e_maps[i][j][1] = m * p_pos_oils2[i] / ((1-pp) * p_pos_v)
                else:
                    if m[pos.i][pos.j] > 0 or (pp == 1 and m[pos.i][pos.j] == 0):
                        self.e_maps[i][j][1] = m * 0
                        self.e_maps[i][j][0] = False
                    else:
                        if m[pos.i][pos.j] > 0:
                            self.e_maps[i][j][1] = m * p_pos_oils1[i] / (pp * p_pos_v)
                        else:
                            self.e_maps[i][j][1] = m * p_pos_oils2[i] / ((1-pp) * p_pos_v)
                # if i == 1 and j == 7:
                #     self.judge.std(f'2pp={pp}, m={self.e_maps[i][j][1][3][8]}, pos={pos}, v={v}, *={p_pos_oils1[i] / (pp * p_pos_v)}, p_pos_v={p_pos_v}, p_pos_oils1[i]={p_pos_oils1[i]}, p_pos_oils2[i]={p_pos_oils2[i]}')
        
        '''
        # 確率が1の場合は全て追加する
        if self.e_maps[i][j][1].max() == 1:
            self.pattern_cnt[i] = 1
            _, m, min_max = ms[j]
            min_i, max_i, min_j, max_j = min_max
            for i2 in range(min_i, max_i+1):
                for j2 in range(min_j, max_j+1):
                    if m[i2][j2] > 0 and self.mined[i2][j2] == 0:
                        self.ans.append(Pos(i2, j2))
                        self.mined[i2][j2] = 1
                        self.found_d += 1
        '''

        # 期待値算出
        # self.pattern_cnt = [p_pos_v for _ in range(self.M)]
        all_e_map = np.zeros((self.N, self.N))
        for i in range(self.M):
            self.oil_maps[i] = np.zeros((self.N, self.N))
            ms = self.e_maps[i]
            for j in range(len(ms)):
                self.oil_maps[i] += ms[j][1]
                all_e_map += ms[j][1]

        # 存在確率算出
        tmp = np.ones((self.N, self.N))
        for i in range(self.M):
            tmp *= 1 - self.oil_maps[i]
        self.pos_prob = np.ones((self.N, self.N)) - tmp
        return all_e_map

    def _update_e_maps(self, pos: Pos):
        # 埋蔵量が0のposに期待値があるmapはFalseに更新
        for i in range(self.M):
            if self.pattern_cnt[i] == 1:
                continue
            ms = self.e_maps[i]
            cnt = 0
            for j in range(len(ms)):
                if not self.e_maps[i][j][0]:
                    continue
                m = ms[j][1]
                if m[pos.i][pos.j] > 0:
                    self.e_maps[i][j][0] = False
                    self.oil_maps[i] -= m
                if self.e_maps[i][j][0]:
                    cnt += 1
                    jj = j
            self.pattern_cnt[i] = cnt
            # cnt==1 つまり、パターンが特定された場合は全て追加
            if cnt == 1:
                _, m, min_max = ms[jj]
                min_i, max_i, min_j, max_j = min_max
                for i in range(min_i, max_i+1):
                    for j in range(min_j, max_j+1):
                        if m[i][j] > 0 and self.mined[i][j] == 0:
                            self.ans.append(Pos(i, j))
                            self.mined[i][j] = 1
                            self.found_d += 1
                        if m[i][j] > 0:
                            self.v_map[i][j] -= 1
                            self.v_map2[i][j] += 1
                            if self.v_map[i][j] == 0:
                                self.all_e_maps = self._update_e_maps(Pos(i, j))
        return self._merge_maps()

    def _sort_map(self, e_map) -> list[list[float, Pos]]:
        sort_poses = []
        for i in range(self.N):
            for j in range(self.N):
                if not self.mined[i][j]:
                    e = e_map[i][j]
                    sort_poses.append((e, Pos(i, j)))
        random.seed(0)
        random.shuffle(sort_poses)
        sort_poses = sorted(sort_poses, key=lambda x:x[0], reverse=True)
        return sort_poses

    def _show_map(self, e_map) -> None:
        e_max = max(map(max, e_map))
        self.judge.comment(f'e_max: {e_max}, median: {np.median(e_map)}, mean: {np.mean(e_map)}')
        for i in range(self.N):
            for j in range(self.N):
                e = min(e_map[i][j], 1)
                G = 255
                if e_map[i][j] == 0:
                    R, B = 255, 255
                elif e_map[i][j] == 1:
                    R, B = 255, 0
                else:
                    R = int(200*(1-e))
                    B = int(200*(1-e))
                # R = int(200*(e_max-e_map[i][j])/e_max)
                # B = int(200*(e_max-e_map[i][j])/e_max)
                self.judge.color(Pos(i, j), f'#{R:02X}{G:02X}{B:02X}')
        # self.judge.std('pos_prob:\n', self.pos_prob)
        # self.judge.std('oil_maps[0]:\n', self.oil_maps[0])
        # self.judge.std('oil_maps[1]:\n', self.oil_maps[1])
        self.judge.std('e_maps[0]:\n', self.e_maps[0][50])
        self.judge.std('e_maps[1]:\n', self.e_maps[1][42])

    def _expected_map(self, poly: Polyomino) -> list[list[bool, list[float]]]:
        # Polyminoの配置のあり得るパターンの期待値を全て保持。boolは配置があり得るかの判断用(Trueがあり得る)
        min_i, max_i = self.N, 0
        min_j, max_j = self.N, 0
        for p in poly.poses:
            min_i = min(p.i, min_i)
            max_i = max(p.i, max_i)
            min_j = min(p.j, min_j)
            max_j = max(p.j, max_j)
        # 平行移動を全パターン試して期待値を求める
        e_maps = []
        base_map = np.zeros((self.N, self.N))
        for p in poly.poses:
            base_map[p.i][p.j] += 1
        base_map /= (self.N-max_i) * (self.N-max_j)  # ADD
        for i in range(self.N-max_i):
            for j in range(self.N-max_j):
                e_maps.append([True, np.roll(base_map, (i, j), axis=(0, 1)), (min_i+i, max_i+i, min_j+j, max_j+j)])
        oil_map = np.zeros((self.N, self.N))
        cnt = 0
        for _, m, _ in e_maps:
            oil_map += m
            cnt += 1
        self.oil_maps.append(oil_map)
        self.pattern_cnt.append(cnt)
        return e_maps
    
    def _merge_maps(self):
        # 存在確率算出
        tmp = np.ones((self.N, self.N))
        for i in range(self.M):
            # tmp *= 1 - self.oil_maps[i]/self.pattern_cnt[i]
            tmp *= 1 - self.oil_maps[i]
        self.pos_prob = np.ones((self.N, self.N)) - tmp
        # 存在確率が1は解答に追加
        for i in range(self.N):
            for j in range(self.N):
                if not self.mined[i][j] and self.pos_prob[i][j] == 1:
                    self.mined[i][j] = 1
                    self.ans.append(Pos(i, j))
                    self.found_d += 1
                # if not self.mined[i][j] and self.pos_prob[i][j] == 0:
                #     self.mined[i][j] = 1
                #     self._update_e_maps(Pos(i, j))
        # 期待値算出
        all_e_map = np.zeros((self.N, self.N))
        for i in range(self.M):
            # all_e_map += self.oil_maps[i] / self.pattern_cnt[i]
            all_e_map += self.oil_maps[i]
        return all_e_map


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
