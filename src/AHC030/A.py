from dataclasses import dataclass
import sys
import numpy as np
import random
import itertools
import math


debug = False


@dataclass
class Pos:
    i: int
    j: int


@dataclass
class Polyomino:
    d: int
    poses: list[Pos]


class Judge:

    def __init__(self, data=None):
        if data is None:
            self.N, self.M, self.e = self._read_initial()
            self.oil_fields = []
            for _ in range(self.M):
                self.oil_fields.append(self._read_oil_field())
            self.v_map = None
            self.cost = 0
        else:
            self.N, self.M, self.e = data[0]
            self.oil_fields = data[1]
            self.v_map = data[2]
            self.cost = data[3]
    
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
        if self.v_map is not None:
            v = self.v_map[poly.poses[0].i][poly.poses[0].j]
            if v > -1:
                return v
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
        if debug:
            print(*message, file=sys.stderr)

    def color(self, p:  Pos, c: str) -> None:
        print(f'#c {p.i} {p.j} {c}')


class Solver:

    def __init__(self):
        self.judge = Judge()
        self.N, self.M, self.e = self.judge.read_initial()
        self.oil_fields = self.judge.read_oil_fields()
        self.oil_maps = []  # 油田ごとの期待値
        self.pattern_cnt = []  # 油田のパターンの残数
        self.mined = [[0]*self.N for _ in range(self.N)]  # 採掘、もしくは、有無が確定した箇所
        self.ans = []  # 解答。埋蔵量がある位置
        self.v_map = [[2*self.M]*self.N for _ in range(self.N)]  # 埋蔵量を保持
        self.v_map2 = [[0]*self.N for _ in range(self.N)]  # 採掘せずに有無が確定した埋蔵量を保持
        self.v_map_for_retry = [[-1]*self.N for _ in range(self.N)]

    def solve(self) -> dict:
        trial_cnt = 0
        sum_d = 0
        self.found_d = 0
        self.e_maps = []  # _expected_mapの結果を保持
        for poly in self.oil_fields:
            sum_d += poly.d
            self.e_maps.append(self._expected_map(poly))
        self.all_e_maps = self._merge_maps()
        self._show_map(self.all_e_maps)
        sorted_poses = self._sort_map(self.all_e_maps)
        while len(sorted_poses) > 0:
            trial_cnt += 1
            self.judge.std('trial cnt', trial_cnt)
            for i in range(len(sorted_poses)):
                e, pos = sorted_poses[i]
                if self.pos_prob[pos.i][pos.j] == 1:
                    self.judge.std('ans append e==1', pos)
                    self.ans.append(pos)
                    self.mined[pos.i][pos.j] = 1
                    self.found_d += 1
                else:
                    break
            if e == 0:  # 埋蔵量の期待値が0だと処理終了
                self.judge.std('end', e, e==0, e>0)
                break
            if self.mined[pos.i][pos.j]:  # 採掘済みはスキップ
                continue
            v = self._mining(pos)
            if self.found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
            sorted_poses = self._sort_map(self.all_e_maps)
            self._show_map(self.all_e_maps)
        ret = self.judge.answer(self.ans)
        self.judge.std('answer', ret)
        # assert ret == 1
        if ret == 0:
            self.judge.std('retry')
            data = [(self.N, self.M, self.e), self.oil_fields, self.v_map_for_retry, self.judge.cost+1]
            result = retry(data)
        else:
            result = {'N': self.N, 'M': self.M, 'e': self.e, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, pos) -> int:
        v = self.judge.query(Polyomino(1, [pos]))
        self.v_map_for_retry[pos.i][pos.j] = v
        if v > 0:
            self.ans.append(pos)
            self.judge.std('ans v > 0', pos)
        self.mined[pos.i][pos.j] = 1
        self.judge.comment(f'query: (1, {pos}), v: {v}')

        # 埋蔵量の情報を保存
        self.all_e_maps = self._update_e_maps_v(pos, v)
        self.found_d += v
        '''
        self.v_map[pos.i][pos.j] = v - self.v_map2[pos.i][pos.j]
        if self.v_map[pos.i][pos.j] == 0:
            self.all_e_maps = self._update_e_maps(pos)
        if v > 0:
            self.ans.append(pos)
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
            self.judge.std('i', i, 'v', v, 'pos', pos, 'pp', pp, 'True cnt', sum([1 for m in ms if m[0]]), [m[3] for m in ms if (m[1][pos.i][pos.j]==1)])
            for j in range(len(ms)):
                m = ms[j][1]
                p = ms[j][3]
                if i == 3 and j == 25:
                    self.judge.std(ms[j][0], ms[j][3])
                if v > 0:
                    '''
                    if pp == 0:
                        self.e_maps[i][j][3] = 0
                        self.e_maps[i][j][0] = False
                    '''
                    # else:
                    if m[pos.i][pos.j] > 0:
                        if pp > 0:
                            self.e_maps[i][j][3] = min(0.99, max(0.01, (p / pp) * (p_pos_oils1[i] / p_pos_v)))
                    else:
                        if pp == 1:
                            self.e_maps[i][j][3] = 0
                            self.e_maps[i][j][0] = False
                        else:
                            self.e_maps[i][j][3] = (p / (1-pp)) * (p_pos_oils2[i] / p_pos_v)
                else:
                    if m[pos.i][pos.j] > 0:
                        self.e_maps[i][j][3] = 0
                        self.e_maps[i][j][0] = False
                    else:
                        # self.judge.std('p_pos_v', p_pos_v, 'p_pos_oils1', p_pos_oils1[i], 'p_pos_oils2', p_pos_oils2[i], 'p', p, 'pp', pp)
                        if pp < 1:
                            self.e_maps[i][j][3] = (p / (1-pp)) * (p_pos_oils2[i] / p_pos_v)
                # if i == 1 and j == 7:
                #     self.judge.std(f'2pp={pp}, m={self.e_maps[i][j][1][3][8]}, pos={pos}, v={v}, *={p_pos_oils1[i] / (pp * p_pos_v)}, p_pos_v={p_pos_v}, p_pos_oils1[i]={p_pos_oils1[i]}, p_pos_oils2[i]={p_pos_oils2[i]}')
        
        # 期待値算出
        # self.pattern_cnt = [p_pos_v for _ in range(self.M)]
        all_e_map = np.zeros((self.N, self.N))
        for i in range(self.M):
            self.oil_maps[i] = np.zeros((self.N, self.N))
            ms = self.e_maps[i]
            for j in range(len(ms)):
                self.oil_maps[i] += ms[j][1] * ms[j][3]
                all_e_map += ms[j][1] * ms[j][3]

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
                p = ms[j][3]
                if m[pos.i][pos.j] > 0:
                    self.e_maps[i][j][0] = False
                    self.oil_maps[i] -= m * p
                else:
                    cnt += 1
                    jj = j
            self.pattern_cnt[i] = cnt
            # cnt==1 つまり、パターンが特定された場合は全て追加
            if cnt == 1:
                _, m, ij = ms[jj]
                for pp in self.oil_fields[i].poses:
                    i2, j2 = ij[0]+pp.i, ij[1]+pp.j
                    if self.mined[i2][j2] == 0:
                        self.judge.std('ans cnt==1', Pos(i2, j2))
                        self.ans.append(Pos(i2, j2))
                        self.mined[i2][j2] = 1
                        self.found_d += 1
                    # 採掘済みで埋蔵量の元が全て特定された位置は他にないためe_mapsを更新
                    self.v_map[i2][j2] -= 1
                    self.v_map2[i2][j2] += 1
                    if self.v_map[i2][j2] == 0:
                        self.all_e_maps = self._update_e_maps(Pos(i2, j2))
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
        if not debug:
            return
        e_max = max(map(max, e_map))
        self.judge.comment(f'e_max: {e_max}, median: {np.median(e_map)}, mean: {np.mean(e_map)}')
        for i in range(self.N):
            for j in range(self.N):
                G = 255
                if e_max > 0:
                    R = int(200*(e_max-e_map[i][j])/e_max)
                    B = int(200*(e_max-e_map[i][j])/e_max)
                if e_map[i][j] == 0 or e_max == 0:
                    R, B = 255, 255
                self.judge.color(Pos(i, j), f'#{R:02X}{G:02X}{B:02X}')
        # self.judge.std('all_e_maps:\n', self.all_e_maps)
        # self.judge.std('pos_prob:\n', self.pos_prob)
        self.judge.std('oil_maps[0]:\n', self.oil_maps[0])
        self.judge.std('oil_maps[1]:\n', self.oil_maps[1])
        '''
        self.judge.std('oil_maps[2]:\n', self.oil_maps[2])
        self.judge.std('oil_maps[3]:\n', self.oil_maps[3])
        self.judge.std('oil_maps[4]:\n', self.oil_maps[4])
        self.judge.std('oil_maps[5]:\n', self.oil_maps[5])
        '''

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
        self.judge.std('base_map\n', base_map)
        base_p = 1 / ((self.N-max_i) * (self.N-max_j))  # ADD
        for i in range(self.N-max_i):
            for j in range(self.N-max_j):
                e_maps.append([True, np.roll(base_map, (i, j), axis=(0, 1)), (i, j), base_p])
        oil_map = np.zeros((self.N, self.N))
        cnt = 0
        for _, m, _, p in e_maps:
            oil_map += m * p
            cnt += 1
        self.oil_maps.append(oil_map)
        self.pattern_cnt.append(cnt)
        return e_maps
    
    def _merge_maps(self):
        # 存在確率、期待値算出
        all_e_map = np.zeros((self.N, self.N))
        tmp = np.ones((self.N, self.N))
        for i in range(self.M):
            tmp *= 1 - self.oil_maps[i] # /self.pattern_cnt[i]  # 存在(しない)確率
            all_e_map += self.oil_maps[i] # / self.pattern_cnt[i]  # 期待値
        self.pos_prob = np.ones((self.N, self.N)) - tmp
        # 存在確率が1は解答に追加
        for i in range(self.N):
            for j in range(self.N):
                if not self.mined[i][j] and self.pos_prob[i][j] == 1:
                    self.mined[i][j] = 1
                    self.ans.append(Pos(i, j))
                    self.judge.std('ans pos_prob==1', Pos(i, j))
                    self.found_d += 1
                '''
                if not self.mined[i][j] and self.pos_prob[i][j] == 0:
                    self.mined[i][j] = 1
                    self.all_e_maps = self._update_e_maps(Pos(i, j))
                '''
        return all_e_map


def retry(data):
    solver = Solver2(data)
    return solver.solve()


class Solver2:

    def __init__(self, v_map_for_retry=None):
        self.judge = Judge(v_map_for_retry)
        self.N, self.M, self.e = self.judge.read_initial()
        self.oil_fields = self.judge.read_oil_fields()
        self.oil_maps = []  # 油田ごとの期待値
        self.pattern_cnt = []  # 油田のパターンの残数
        self.mined = [[0]*self.N for _ in range(self.N)]  # 採掘、もしくは、有無が確定した箇所
        self.ans = []  # 解答。埋蔵量がある位置
        self.v_map = [[2*self.M]*self.N for _ in range(self.N)]  # 埋蔵量を保持
        self.v_map2 = [[0]*self.N for _ in range(self.N)]  # 採掘せずに有無が確定した埋蔵量を保持

    def solve(self) -> dict:
        sum_d = 0
        self.found_d = 0
        self.e_maps = []  # _expected_mapの結果を保持
        for poly in self.oil_fields:
            sum_d += poly.d
            self.e_maps.append(self._expected_map(poly))
        self.all_e_maps = self._merge_maps()
        self._show_map(self.all_e_maps)
        sorted_poses = self._sort_map(self.pos_prob)
        while len(sorted_poses) > 0:
            e, pos = sorted_poses[0]
            if e == 0:  # 埋蔵量の期待値が0だと処理終了
                break
            if self.mined[pos.i][pos.j]:  # 採掘済みはスキップ
                continue
            v = self._mining(pos)
            self.v_map[pos.i][pos.j] = v - self.v_map2[pos.i][pos.j]
            if self.v_map[pos.i][pos.j] == 0:
                self.all_e_maps = self._update_e_maps(pos)
            self.found_d += v
            if self.found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
            sorted_poses = self._sort_map(self.pos_prob)
        ret = self.judge.answer(self.ans)
        assert ret == 1
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, pos) -> int:
        v = self.judge.query(Polyomino(1, [pos]))
        self.mined[pos.i][pos.j] = 1
        self.judge.comment(f'query: (1, {pos}), v: {v}')
        if v > 0:
            self.ans.append(pos)
        else:
            # 埋蔵量の期待値を更新
            self.all_e_maps = self._update_e_maps(pos)
            # self._show_map(self.all_e_maps)
        return v

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
                else:
                    cnt += 1
                    jj = j
            self.pattern_cnt[i] = cnt
            # cnt==1 つまり、パターンが特定された場合は全て追加
            if cnt == 1:
                _, m, ij = ms[jj]
                for pp in self.oil_fields[i].poses:
                    i2, j2 = ij[0]+pp.i, ij[1]+pp.j
                    if self.mined[i2][j2] == 0:
                        self.ans.append(Pos(i2, j2))
                        self.mined[i2][j2] = 1
                        self.found_d += 1
                    self.v_map[i2][j2] -= 1
                    self.v_map2[i2][j2] += 1
                    if self.v_map[i2][j2] == 0:
                        self.all_e_maps = self._update_e_maps(Pos(i2, j2))
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
                G = 255
                if e_max > 0:
                    R = int(200*(e_max-e_map[i][j])/e_max)
                    B = int(200*(e_max-e_map[i][j])/e_max)
                if e_map[i][j] == 0 or e_max == 0:
                    R, B = 255, 255
                self.judge.color(Pos(i, j), f'#{R:02X}{G:02X}{B:02X}')

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
        for i in range(self.N-max_i):
            for j in range(self.N-max_j):
                e_maps.append([True, np.roll(base_map, (i, j), axis=(0, 1)), (i, j)])
        oil_map = np.zeros((self.N, self.N))
        cnt = 0
        for _, m, _ in e_maps:
            oil_map += m
            cnt += 1
        self.oil_maps.append(oil_map)
        self.pattern_cnt.append(cnt)
        return e_maps
    
    def _merge_maps(self):
        # 存在確率、期待値算出
        all_e_map = np.zeros((self.N, self.N))
        tmp = np.ones((self.N, self.N))
        for i in range(self.M):
            tmp *= 1 - self.oil_maps[i]/self.pattern_cnt[i]  # 存在(しない)確率
            all_e_map += self.oil_maps[i] / self.pattern_cnt[i]  # 期待値
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
        return all_e_map


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
