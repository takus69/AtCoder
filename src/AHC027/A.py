import queue
import sys
import random
import itertools
sys.setrecursionlimit(1000000)


class Solver:
    def __init__(self):
        self.init()
        self.visited_cnt = 0
        self.DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.DIR = 'RDLU'
        self.now_i, self.now_j = 0, 0
        self.ans = ''
        random.seed(0)
        self.dir_pattern = [0, 1, 2, 3]

    def init(self):
        self.N = int(input())
        self.h = [input() for _ in range(self.N-1)]
        self.v = [input() for _ in range(self.N)]
        self.d = [list(map(int, input().split())) for _ in range(self.N)]
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]

    def go_all(self, i, j):
        if not self.visited[i][j]:
            self.visited[i][j] = True
            self.visited_cnt += 1
            # print('visited', i, j, self.visited_cnt, sum([sum([1 for b in self.visited[i] if b]) for i in range(len(self.visited))]))
        # for dir in random.sample(range(4), 4):
        for dir in self.dir_pattern:
            di, dj = self.DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < self.N and 0 <= j2 < self.N and not self.visited[i2][j2]:
                if di == 0 and self.v[i][min(j, j2)] == '0' or dj == 0 and self.h[min(i, i2)][j] == '0':
                    self.ans += self.DIR[dir]
                    self.now_i, self.now_j = i2, j2
                    # print('now', self.now_i, self.now_j)
                    self.go_all(i2, j2)
                    if self.visited_cnt < self.N**2:
                        self.ans += self.DIR[(dir + 2) % 4]
                        self.now_i += self.DIJ[(dir + 2) % 4][0]
                        self.now_j += self.DIJ[(dir + 2) % 4][1]
                        # print('now', self.now_i, self.now_j)
                    else:
                        break
    
    def short_path(self, frm, to):
        '''
        frmからtoへの最短経路のパスを返す
        '''
        f_i, f_j = frm[0], frm[1]
        q = queue.Queue()
        paths = {(f_i, f_j): (0, '')}  # 地点(i, j)の最短移動回数と移動方法を保持
        q.put((f_i, f_j))
        while not q.empty():
            (i, j) = q.get()
            mv_cnt, mv_path = paths[(i, j)]
            for dir in range(4):
                di, dj = self.DIJ[dir]
                i2 = i + di
                j2 = j + dj
                if 0 <= i2 < self.N and 0 <= j2 < self.N:
                    if di == 0 and self.v[i][min(j, j2)] == '0' or dj == 0 and self.h[min(i, i2)][j] == '0':
                        if (i2, j2) in paths.keys():
                            if mv_cnt+1 < paths[(i2, j2)][0]:
                                paths[(i2, j2)] = (mv_cnt+1, mv_path+self.DIR[dir])
                                q.put((i2, j2))
                        else:
                            paths[(i2, j2)] = (mv_cnt+1, mv_path+self.DIR[dir])
                            q.put((i2, j2))
        return paths[to][1]

    def reset(self):
        self.visited_cnt = 0
        self.now_i, self.now_j = 0, 0
        self.ans = ''
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]

    def solve(self):
        # print('now', self.now_i, self.now_j)
        ans = ''
        score = None
        '''
        for i in range(500):
            self.go_all(self.now_i, self.now_j)
            self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
            score2 = self.evaluate()
            if score is None:
                score = score2
                ans = self.ans
            elif score > score2:
                score = score2
                ans = self.ans
            self.reset()
        '''
        patterns = itertools.permutations([0, 1, 2, 3], 4)
        for p in patterns:
            self.dir_pattern = p
            self.go_all(self.now_i, self.now_j)
            self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
            score2 = self.evaluate()
            if score is None:
                score = score2
                ans = self.ans
            elif score > score2:
                score = score2
                ans = self.ans
            self.reset()
        self.submission(ans)
        return score

    def submission(self, ans):
        print(ans)

    def evaluate(self):
        i, j = 0, 0
        passes = {}
        cnt = 0
        self.rev = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
        for a in self.ans:
            dir = self.rev[a]
            cnt += 1
            di, dj = self.DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if (i2, j2) in passes.keys():
                passes[(i2, j2)].append(cnt)
            else:
                passes[(i2, j2)] = [cnt]
            i, j = i2, j2
        L = len(self.ans)
        score = 0
        for i in range(self.N):
            for j in range(self.N):
                d = self.d[i][j]
                d1 = (L - passes[(i, j)][-1]) * d
                p1 = 0
                for p2 in passes[(i, j)] + [L]:
                    d2 = d1 + d * (p2-p1-1)
                    score += (d1+d2) * (p2-p1) / 2
                    d1 = 0
                    p1 = p2
        return round(score / L)


if __name__ == '__main__':
    solver = Solver()
    solver.solve()
