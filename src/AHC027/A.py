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

    def go_all(self, i, j):
        # 移動できる箇所を確認し、3箇所移動可能ならパターンを切り替え
        can_mv_cnt = 0
        for dir in self.dir_pattern:
            di, dj = self.DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < self.N and 0 <= j2 < self.N and not self.visited[i2][j2]:
                if di == 0 and self.v[i][min(j, j2)] == '0' or dj == 0 and self.h[min(i, i2)][j] == '0':
                    can_mv_cnt += 1
        # 3箇所移動可能かつ、切り替えてよいかつ、次のパターンがある場合に切り替え
        if can_mv_cnt == 3 and self.switch_flag and self.switch_cnt < len(self.next_pattern):
            self.dir_pattern = self.next_pattern[self.switch_cnt]
            self.switch_flag = False
            self.switch_cnt += 1
        elif can_mv_cnt < 3 and not self.switch_flag:
            self.switch_flag = True
        # 訪問箇所の個数を確認
        if not self.visited[i][j]:
            self.visited[i][j] = True
            self.visited_cnt += 1
            # print('visited', i, j, self.visited_cnt, sum([sum([1 for b in self.visited[i] if b]) for i in range(len(self.visited))]))
        # 次の移動箇所を再帰的に実施
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
        start = time.time()
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
        self.patterns = itertools.permutations([0, 1, 2, 3], 4)  # RDLU
        results = []  # (スコア、パターンの組み合わせ、出力)を保持
        for p1 in [[0, 1, 2, 3], [1, 0, 2, 3]]:  # 初期はRDかDRから始める
            for p2 in self.patterns:  # 最初の分岐でパターンを入れ替える
                self.dir_pattern = p1
                self.next_pattern = [p2]
                self.switch_flag = True
                self.switch_cnt = 0
                self.go_all(self.now_i, self.now_j)
                self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
                score2 = self.evaluate()
                results.append((score2, [p1, p2], self.ans))
                if score is None:
                    score = score2
                    ans = self.ans
                elif score > score2:
                    score = score2
                    ans = self.ans
                self.reset()
        results = sorted(results, key=lambda x: x[0])
        # print(results)
        pre_score = 0
        trial_cnt = 0
        for score2, patterns, _ in results:
            if pre_score == score2:
                continue
            trial_cnt += 1
            if trial_cnt > 2:
                break
            self.patterns = itertools.permutations([0, 1, 2, 3], 4)  # RDLU
            for p in self.patterns:  # 最初の分岐でパターンを入れ替える
                self.dir_pattern = patterns[0]
                self.next_pattern = patterns[1:] + [p]
                self.switch_flag = True
                self.switch_cnt = 0
                self.go_all(self.now_i, self.now_j)
                self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
                score2 = self.evaluate()
                results.append((score2, [self.dir_pattern] + self.next_pattern, self.ans))
                if score is None:
                    score = score2
                    ans = self.ans
                elif score > score2:
                    score = score2
                    ans = self.ans
                self.reset()
                if time.time() - start > 1.5:
                    break
            pre_score = score2
            if time.time() - start > 1.5:
                break
        # print(results)
        '''
        for p in self.patterns:
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
        '''
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
