from dataclasses import dataclass
import sys
import numpy as np


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

    def solve(self) -> dict:
        sum_d = 0
        self.e_maps = []  # _expected_mapの結果を保持
        for poly in self.oil_fields:
            sum_d += poly.d
            self.e_maps.append(self._expected_map(poly))
        self.all_e_maps = self._merge_maps(self.e_maps)
        self._show_map(self.all_e_maps)
        self.ans = []
        found_d = 0
        sorted_poses = self._sort_map(self.all_e_maps)
        for e, pos in sorted_poses:
            e = self.all_e_maps[pos.i][pos.j]
            if e == 0:  # 埋蔵量の期待値があるところのみ計測
                continue
            v = self._mining(pos)
            found_d += v
            if found_d == sum_d:  # 油田が全て見つかったら処理終了
                break
        ret = self.judge.answer(self.ans)
        assert ret == 1
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _mining(self, pos) -> int:
        self.judge.comment(f'query: (1, pos)')
        v = self.judge.query(Polyomino(1, [pos]))
        if v > 0:
            self.ans.append(pos)
        else:
            # 埋蔵量の期待値を更新
            self.all_e_maps = self._update_e_maps(pos)
        return v
    
    def _update_e_maps(self, pos: Pos):
        # 埋蔵量が0のposに期待値があるmapはFalseに更新
        for i in range(self.M):
            ms = self.e_maps[i]
            for j in range(len(ms)):
                m = ms[j][1]
                if m[pos.i][pos.j] > 0:
                    self.e_maps[i][j][0] = False
        return self._merge_maps(self.e_maps)

    def _sort_map(self, e_map) -> list[list[float, Pos]]:
        sort_poses = []
        for i in range(self.N):
            for j in range(self.N):
                e = e_map[i][j]
                sort_poses.append((e, Pos(i, j)))
        sort_poses = sorted(sort_poses, key=lambda x:x[0], reverse=True)
        return sort_poses

    def _show_map(self, e_map) -> None:
        e_max = max(map(max, e_map))
        self.judge.comment(f'e_max: {e_max}')
        for i in range(self.N):
            for j in range(self.N):
                R = 255
                G = int(200*(e_max-e_map[i][j])/e_max)
                B = int(200*(e_max-e_map[i][j])/e_max)
                if e_map[i][j] == 0:
                    G, B = 255, 255
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
        base_map /= poly.d
        for i in range(self.N-max_i):
            for j in range(self.N-max_j):
                e_maps.append([True, np.roll(base_map, (i, j), axis=(0, 1))])
        return e_maps
    
    def _merge_maps(self, e_maps: list[list]):
        all_e_map = np.zeros((self.N, self.N))
        for ms in e_maps:
            tmp = np.zeros((self.N, self.N))
            cnt = 0
            for b, m in ms:
                if b:
                    cnt += 1
                    tmp += m
            if cnt > 0:
                all_e_map += tmp / cnt
        return all_e_map


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()
