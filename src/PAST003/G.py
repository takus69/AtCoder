import queue

N, X, Y = map(int, input().split())
# 障害物-1, 通過済み: 現時点の最小の移動回数
xy = {}
# (0, 0), (X, Y)の範囲か、障害物の最大+1まで探索する
min_x = min(0, X)
max_x = max(0, X)
min_y = min(0, Y)
max_y = max(0, Y)
for _ in range(N):
    xi, yi = map(int, input().split())
    xy[(xi, yi)] = -1
    min_x = min(min_x, xi-1)
    max_x = max(max_x, xi+1)
    min_y = min(min_y, yi-1)
    max_y = max(max_y, yi+1)


# 関数定義
def add_queue(q, x, y):
    if min_x <= x and x <= max_x and min_y <= y and y <= max_y:
        if not (x, y) in xy:
            q.put((x, y))
            xy[(x, y)] = -2


def cal_dist(x, y):
    ret = 10**9
    if (x, y) in xy:
        if xy[(x, y)] > -1:
            # print(x, y, xy[(x, y)])
            ret = xy[(x, y)] + 1
    return ret


q = queue.Queue()
q.put((0, 0))
cnt = 0
while not q.empty():
    now = q.get()
    cnt += 1
    # print(cnt, now)
    # 隣接を追加(金移動可能な範囲)
    x = now[0]
    y = now[1]
    add_queue(q, now[0]+1, now[1]+1)
    add_queue(q, now[0], now[1]+1)
    add_queue(q, now[0]-1, now[1]+1)
    add_queue(q, now[0]+1, now[1])
    add_queue(q, now[0]-1, now[1])
    add_queue(q, now[0], now[1]-1)

    # 最小移動回数を算出
    if (x, y) == (0, 0):
        xy[(0, 0)] = 0
    else:
        # print('xxx', x, y)
        xy[(x, y)] = 10**9
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x-1, y-1))
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x, y-1))
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x+1, y-1))
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x-1, y))
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x+1, y))
        xy[(x, y)] = min(xy[(x, y)], cal_dist(x, y+1))

if (X, Y) in xy:
    ans = xy[(X, Y)]
else:
    ans = -1
print(ans)
