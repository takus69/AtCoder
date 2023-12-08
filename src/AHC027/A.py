import queue
import sys
import random
import itertools
import time
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

    def go(self, i, j):
        self.go_cnt += 1
        # 訪問箇所の個数を確認
        if not self.visited[i][j]:
            self.visited[i][j] = True
            self.visited_cnt += 1
        # 移動できる箇所を確認し、3箇所移動可能ならパターンを切り替え
        can_mv_cnt = 0
        for dir in self.dir_pattern:
            di, dj = self.DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < self.N and 0 <= j2 < self.N and not self.visited[i2][j2]:
                if di == 0 and self.v[i][min(j, j2)] == '0' or dj == 0 and self.h[min(i, i2)][j] == '0':
                    can_mv_cnt += 1
        # 移動箇所がなくなったら終了
        if can_mv_cnt == 0:
            self.go_flag = False
            return
        # 次の移動箇所を再帰的に実施
        for dir in self.dir_pattern:
            di, dj = self.DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < self.N and 0 <= j2 < self.N and not self.visited[i2][j2]:
                if di == 0 and self.v[i][min(j, j2)] == '0' or dj == 0 and self.h[min(i, i2)][j] == '0':
                    self.ans += self.DIR[dir]
                    self.now_i, self.now_j = i2, j2
                    self.go(i2, j2)
                    if not self.go_flag:
                        break

    def short_path_not_visited(self, frm):
        '''
        frmから未訪問の一番近いマスへ移動
        '''
        self.short_cnt += 1
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
        d = self.N**2
        to = (0, 0)
        for k, v in paths.items():
            if v[0] < d and not self.visited[k[0]][k[1]]:
                d = v[0]
                to = k
        self.now_i, self.now_j = to[0], to[1]
        self.visited[self.now_i][self.now_j] = True
        self.visited_cnt += 1
        return paths[to][1]

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
        # 初期化
        ans = ''
        score = None
        start = time.time()

        self.patterns = itertools.permutations([0, 1, 2, 3], 4)  # RDLU
        self.trial_cnt = 0
        self.go_cnt = 0
        self.short_cnt = 0
        for p2 in self.patterns:  # 最初の分岐でパターンを入れ替える
            for p1 in [[0, 1, 2, 3], [1, 0, 2, 3]]:  # 初期はRDかDRから始める
                self.trial_cnt += 1
                self.dir_pattern = p1
                self.next_pattern = [p2]
                self.switch_cnt = 0
                while self.visited_cnt < self.N**2:
                    self.go_flag = True
                    self.go(self.now_i, self.now_j)
                    self.ans += self.short_path_not_visited((self.now_i, self.now_j))
                    if self.switch_cnt < len(self.next_pattern):
                        self.dir_pattern = self.next_pattern[self.switch_cnt]
                    self.switch_cnt += 1
                self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
                score2 = self.evaluate()
                if score is None:
                    score = score2
                    ans = self.ans
                elif score > score2:
                    score = score2
                    ans = self.ans
                self.reset()
                if time.time() - start > 1.5:
                    break
            if time.time() - start > 1.5:
                break
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
