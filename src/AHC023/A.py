from queue import Queue


def read_input():
    T, H, W, i0 = map(int, input().split())
    h = [[False]*W for _ in range(H-1)]
    for i in range(H-1):
        in_h = input()
        for j in range(W):
            if in_h[j] == '1':
                h[i][j] = True
            else:
                h[i][j] = False
    v = [[False]*(W-1) for _ in range(H)]
    for i in range(H):
        in_w = input()
        for j in range(W-1):
            if in_w[j] == '1':
                v[i][j] = True
            else:
                v[i][j] = False
    K = int(input())
    S, D = [], []
    for _ in range(K):
        s, d = map(int, input().split())
        S.append(s)
        D.append(d)
    return T, H, W, i0, h, v, K, S, D


def reachable(i, j, adj, used, i0):
    if used[i][j] or used[i0][0]:
        return False
    elif i == i0 and j == 0:
        return True
    
    # 深さ優先探索で到達できるかを確認
    q = Queue()
    q.put((i0, 0))
    visited = [[False]*W for _ in range(H)]
    visited[i0][0] = True
    while True:
        i1, j1 = q.get()
        for i2, j2 in adj[(i1, j1)]:
            if i2 == i and j2 == j:
                return True
            elif not used[i2][j2] and not visited[i2][j2]:
                visited[i2][j2] = True
                q.put((i2, j2))
        if q.empty():
            break
    return False


def is_valid_plan(plan, adj, i0):
    plant_list = {t: [] for t in range(1, T+1)}
    harvest_list = {t: [] for t in range(1, T+1)}
    for p in plan:
        plant_list[p.s].append(p)
        harvest_list[D[p.k]].append(p)
    used = [[False]*W for _ in range(H)]
    for t in range(1, T+1):
        # 植える時に農機が行けるか)
        for p in plant_list[t]:
            if not reachable(p.i, p.j, adj, used, i0):
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
            if not reachable(p.i, p.j, adj, used, i0):
                return False
    return True


class Plan:
    def __init__(self, k, i, j, s):
        self.k = k
        self.i = i
        self.j = j
        self.s = s


if __name__ == '__main__':
    T, H, W, i0, h, v, K, S, D = read_input()
    # 水路を考慮した移動可能な経路作成
    adj = {}
    for i in range(H):
        for j in range(W):
            adj[(i,j)] = []
    for i in range(H):
        for j in range(W):
            if i+1 < H and not h[i][j]:
                adj[(i,j)].append((i+1,j))
                adj[(i+1,j)].append((i,j))
            if j+1 < W and not v[i][j]:
                adj[(i,j)].append((i,j+1))
                adj[(i,j+1)].append((i,j))
    # 計画作成
    plan = []
    for k in range(min(K, 10)):
        found = False
        for i in range(H):
            for j in range(W):
                plan.append(Plan(k, i, j, S[k]))
                if not is_valid_plan(plan, adj, i0):
                    plan.pop()
                else:
                    found = True
                    break
            if found:
                break

    print(len(plan))
    for p in plan:
        print(p.k+1, p.i, p.j, p.s)
