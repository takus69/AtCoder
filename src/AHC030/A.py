from dataclasses import dataclass
import sys


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
        e_maps = []
        for poly in self.oil_fields:
            sum_d += poly.d
            e_maps.append(self._expected_map(poly))
        all_e_maps = self._merge_maps(e_maps)
        ans = []
        found_d = 0
        for i in range(self.N):
            for j in range(self.N):
                if all_e_maps[i][j] == 0:
                    continue
                v = self.judge.query(Polyomino(1, [Pos(i, j)]))
                found_d += v
                if v > 0:
                    ans.append(Pos(i, j))
                if found_d == sum_d:
                    break
        ret = self.judge.answer(ans)
        assert ret == 1
        result = {'N': self.N, 'M': self.M, 'e': self.e, 'cost': self.judge.cost, 'score': self.judge.cost*(10**6)}
        return result
    
    def _expected_map(self, poly: Polyomino) -> list[float]:
        min_i, max_i = self.N, 0
        min_j, max_j = self.N, 0
        for p in poly.poses:
            min_i = min(p.i, min_i)
            max_i = max(p.i, max_i)
            min_j = min(p.j, min_j)
            max_j = max(p.j, max_j)
        # 平行移動を全パターン試して期待値を求める
        e_map = [[0]*self.N for _ in range(self.N)]
        for i in range(self.N-max_i):
            for j in range(self.N-max_j):
                for p in poly.poses:
                    e_map[p.i+i][p.j+j] += 1
        for i in range(self.N):
            for j in range(self.N):
                e_map[i][j] /= poly.d
        return e_map
    
    def _merge_maps(self, e_maps: list[list]):
        all_e_map = [[0]*self.N for _ in range(self.N)]
        for m in e_maps:
            for i in range(self.N):
                for j in range(self.N):
                    all_e_map[i][j] += m[i][j]
        return all_e_map


def main():
    solver = Solver()
    result = solver.solve()
    print(result, file=sys.stderr)


if __name__ == "__main__":
    main()