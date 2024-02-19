from dataclasses import dataclass
import sys
import numpy as np
import random


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
            if False: # self.M > 10 and self.found_d < sum_d/3: # and self.e > random.random():
                i = int(random.expovariate(lambd=1))
                # i = int(random.random()*(len(sorted_poses)/2))
                i = min(len(sorted_poses)-1, i)
            else:
                i = 0
            e, pos = sorted_poses[i]
            if e == 0:  # 埋蔵量の期待値が0だと処理終了
                break
            if self.mined[pos.i][pos.j]:  # 採掘済みはスキップ
                continue
            v = self._mining(pos)
            if self.found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
            sorted_poses = self._sort_map(self.pos_prob)
        ret = self.judge.answer(self.ans)
        assert ret == 1
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'd': sum_d, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, pos) -> int:
        v = self.judge.query(Polyomino(1, [pos]))
        self.mined[pos.i][pos.j] = 1
        self.judge.comment(f'query: (1, {pos}), v: {v}')

        # 埋蔵量の情報を保存
        self.v_map[pos.i][pos.j] = v - self.v_map2[pos.i][pos.j]
        self.found_d += v
        if v > 0:
            self.ans.append(pos)
            if self.v_map[pos.i][pos.j] == 0:
                self.all_e_maps = self._update_e_maps(pos)
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
                    if e > 0:
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
                '''
                if not self.mined[i][j] and self.pos_prob[i][j] == 0:
                    self.mined[i][j] = 1
                    self.all_e_maps = self._update_e_maps(Pos(i, j))
                '''
        return all_e_map


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
