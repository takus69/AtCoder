W, H = map(int, input().split())
N = int(input())
p, q = [], []
for _ in range(N):
    pp, qq = map(int, input().split())
    p.append(pp)
    q.append(qq)
A = int(input())
a = [0]
a += list(map(int, input().split()))
a.append(W)
B = int(input())
b = [0]
b += list(map(int, input().split()))
b.append(H)
# print(a, b)

cnt = {}
for i in range(N):
    pi, qi = p[i], q[i]
    # イチゴが入るx座標を確認
    s, e = 0, A+1
    # print(i, s, e, pi, qi, 'x')
    while (e - s >= 1):
        m = (s + e) // 2
        # print('x', s, e, m)
        if a[m] < pi:
            s = m
        else:
            e = m
        if e - s == 1:
            break
    ps = s
    # y座標
    s, e = 0, B+1
    # print(i, s, e, 'y')
    while (e - s >= 1):
        m = (s + e) // 2
        # print('y', s, e, m)
        if b[m] < qi:
            s = m
        else:
            e = m
        if e - s == 1:
            break
    qs = s
    cnt[(ps, qs)] = cnt.get((ps, qs), 0) + 1

min_cnt, max_cnt = 10**6, 0
# print(cnt, len(cnt))
for k, v in cnt.items():
    min_cnt = min(min_cnt, v)
    max_cnt = max(max_cnt, v)
if len(cnt) < (A+1)*(B+1):
    min_cnt = 0

print(min_cnt, max_cnt)
