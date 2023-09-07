from queue import Queue
import os


class Solver:
    def __init__(self):
        self.in_file = None
        self.out_file = None

    def read_input(self):
        self.T, self.H, self.W, self.i0 = map(int, self.input().split())
        self.h = [[False]*self.W for _ in range(self.H-1)]
        for i in range(self.H-1):
            in_h = self.input()
            for j in range(self.W):
                if in_h[j] == '1':
                    self.h[i][j] = True
                else:
                    self.h[i][j] = False
        self.v = [[False]*(self.W-1) for _ in range(self.H)]
        for i in range(self.H):
            in_w = self.input()
            for j in range(self.W-1):
                if in_w[j] == '1':
                    self.v[i][j] = True
                else:
                    self.v[i][j] = False
        self.K = int(self.input())
        self.S, self.D = [], []
        for _ in range(self.K):
            s, d = map(int, self.input().split())
            self.S.append(s)
            self.D.append(d)
        self.KSD = []
        for i in range(self.K):
            self.KSD.append((i, self.S[i], self.D[i]))
        self.KSD = sorted(self.KSD, key=lambda x:x[2]-x[1], reverse=True)
        self.KSD = sorted(self.KSD[:self.H*self.W], key=lambda x:x[2], reverse=True)

        # 水路を考慮した移動可能な経路作成
        self.adj = {}
        for i in range(self.H):
            for j in range(self.W):
                self.adj[(i,j)] = []
        for i in range(self.H):
            for j in range(self.W):
                if i+1 < self.H and not self.h[i][j]:
                    self.adj[(i,j)].append((i+1,j))
                    self.adj[(i+1,j)].append((i,j))
                if j+1 < self.W and not self.v[i][j]:
                    self.adj[(i,j)].append((i,j+1))
                    self.adj[(i,j+1)].append((i,j))

        self.search_distances()
        
    def search_distances(self):
        # 幅優先探索で区画の距離を測定
        q = Queue()
        q.put((self.i0, 0))
        visited = [[False]*self.W for _ in range(self.H)]
        visited[self.i0][0] = True
        self.places = {1: [(self.i0, 0)]}
        self.distances = {(self.i0, 0): 1}
        while True:
            i1, j1 = q.get()
            for i2, j2 in self.adj[(i1, j1)]:
                if not visited[i2][j2]:
                    dist = self.distances[(i1,j1)]+1
                    self.distances[(i2,j2)] = dist
                    visited[i2][j2] = True
                    q.put((i2, j2))
                    if dist in self.places.keys():
                        self.places[dist].append((i2,j2))
                    else:
                        self.places[dist] = [(i2,j2)]
            if q.empty():
                break

    def set_filepath(self, in_filename, out_filename):
        self.in_file = open(in_filename, 'r')
        self.out_file = open(out_filename, 'w')

    def input(self):
        if self.in_file is None:
            return input()
        else:
            return self.in_file.readline()

    def reachable(self, i, j, used):
        if used[i][j] or used[self.i0][0]:
            return False
        elif i == self.i0 and j == 0:
            return True
        
        # 深さ優先探索で到達できるかを確認
        q = Queue()
        q.put((self.i0, 0))
        visited = [[False]*self.W for _ in range(self.H)]
        visited[self.i0][0] = True
        while True:
            i1, j1 = q.get()
            for i2, j2 in self.adj[(i1, j1)]:
                if i2 == i and j2 == j:
                    return True
                elif not used[i2][j2] and not visited[i2][j2]:
                    visited[i2][j2] = True
                    q.put((i2, j2))
            if q.empty():
                break
        return False


    def is_valid_plan(self, plan):
        plant_list = {t: [] for t in range(1, self.T+1)}
        harvest_list = {t: [] for t in range(1, self.T+1)}
        for p in plan:
            plant_list[p.s].append(p)
            harvest_list[self.D[p.k]].append(p)
        used = [[False]*self.W for _ in range(self.H)]
        for t in range(1, self.T+1):
            # 植える時に農機が行けるか)
            for p in plant_list[t]:
                if not self.reachable(p.i, p.j, used):
                    return False
            # (i,j)に植えられていないか、植えられてなければ植える
            for p in plant_list[t]:
                if used[p.i][p.j]:
                    return False
                else:
                    used[p.i][p.j] = True
            # 収穫する(usedを解除)
            for p in harvest_list[t]:
                used[p.i][p.j] = False
            # 収穫時に農機が行けるか
            for p in harvest_list[t]:
                if not self.reachable(p.i, p.j, used):
                    return False
        return True

    def make_plan(self):
        # 計画作成
        self.plan = []
        dist_keys = sorted(self.places.keys(), reverse=True)
        i = 0
        for dist in dist_keys:
            for p in self.places[dist]:
                self.plan.append(Plan(self.KSD[i][0], p[0], p[1], 1))
                # if not self.is_valid_plan(self.plan):
                #     print(f'{i}: {self.KSD[i][0]}, {p[0]}, {p[1]}, 1 is not valid')
                i += 1
                if i >= self.K:
                    break
            if i >= self.K:
                break
        '''
        for k in range(min(self.K, 20)):
            found = False
            for i in range(self.H):
                for j in range(self.W):
                    self.plan.append(Plan(k, i, j, self.S[k]))
                    if not self.is_valid_plan(self.plan):
                        self.plan.pop()
                    else:
                        found = True
                        break
                if found:
                    break
        '''

    def print(self, s):
        if self.out_file is None:
            print(s)
        else:
            self.out_file.write(s + '\n')

    def submission(self):
        self.print(str(len(self.plan)))
        for p in self.plan:
            self.print('{} {} {} {}'.format(p.k+1, p.i, p.j, p.s))
        if self.in_file is not None:
            self.in_file.close()
            self.out_file.close()
    
    def evaluate(self):
        score = 0
        for p in self.plan:
            score += self.D[p.k] - self.S[p.k] + 1
        score *= 1000000/(self.H*self.W*self.T)
        score = int(score)
        return score


class Plan:
    def __init__(self, k, i, j, s):
        self.k = k
        self.i = i
        self.j = j
        self.s = s


if __name__ == '__main__':
    solver = Solver()
    solver.read_input()
    solver.make_plan()
    solver.submission()
