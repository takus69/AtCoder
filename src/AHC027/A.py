import queue
import sys
sys.setrecursionlimit(1000000)


class Solver:
    def __init__(self):
        self.init()
        self.visited_cnt = 0
        self.DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.DIR = "RDLU"
        self.now_i, self.now_j = 0, 0
        self.ans = ''

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
        for dir in range(4):
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

    def solve(self):
        # print('now', self.now_i, self.now_j)
        self.go_all(self.now_i, self.now_j)
        self.ans += self.short_path((self.now_i, self.now_j), (0, 0))
        self.submission()

    def submission(self):
        print(self.ans)

    def evaluate(self):
        None

if __name__ == '__main__':
    solver = Solver()
    solver.solve()
