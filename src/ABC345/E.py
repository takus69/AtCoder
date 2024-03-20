from dataclasses import dataclass
from copy import deepcopy

N, K = map(int, input().split())
C, V = [], []
for _ in range(N):
    c, v = map(int, input().split())
    C.append(c)
    V.append(v)

@dataclass
class VC:
    v: int
    c: int

class Top2:
    def __init__(self):
        self.vc1 = VC(-1, -1)
        self.vc2 = VC(-1, -1)

    def add_vc(self, vc):
        if self.vc2.v < vc.v:
            self.vc2, vc = vc, self.vc2
        if self.vc1.v < self.vc2.v:
            self.vc1, self.vc2 = self.vc2, self.vc1
        if self.vc1.c == self.vc2.c:
            self.vc2, vc = vc, self.vc2

    def add_top2(self, top2):
        self.add_vc(top2.vc1)
        self.add_vc(top2.vc2)

    def __repr__(self):
        return f'Top2(vc1: {self.vc1}, vc2: {self.vc2})'


dp = [Top2() for _ in range(K+1)]
dp[0].add_vc(VC(0, -1))

for i in range(1, N+1):
    v, c = V[i-1], C[i-1]
    old = dp
    dp = [Top2() for _ in range(K+1)]
    for j in range(K+1):
        if old[j].vc1.c == c:
            if old[j].vc2.v >= 0:
                dp[j].add_vc(VC(old[j].vc2.v + v, c))
        else:
            if old[j].vc1.v >= 0:
                dp[j].add_vc(VC(old[j].vc1.v + v, c))
        if j > 0:
            dp[j].add_top2(old[j-1])

print(dp[K].vc1.v)
