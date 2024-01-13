import sys
import random

random.seed(0)

N, M = map(int, input().split())
si, sj = map(int, input().split())
A = []
for _ in range(N):
    A.append(input())
t = []
for _ in range(M):
    t.append(input())

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pos = {a: [] for a in alphabets}
for i in range(N):
    for j in range(N):
        a = A[i][j]
        pos[a].append((i, j))
nearest = {}
for i in range(N):
    for j in range(N):
        nearest[(i, j)] = {}  # A: (i2, j2, dist)
        for a in alphabets:
            cost = 2*N
            for i2, j2 in pos[a]:
                tmp = abs(i-i2)+abs(j-j2)+1
                if cost > tmp:
                    cost = tmp
                    nearest[(i, j)][a] = [i2, j2, cost]

# 順番を決める
pre_next = {ti: [None, 0, False, False] for ti in t}
for k in range(5, 0, -1):
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if t[i][-k:] == t[j][:k]:
                if not pre_next[t[i]][2] and not pre_next[t[j]][3]:
                    pre_next[t[i]] = [t[j], k, True, pre_next[t[i]][3]]
                    pre_next[t[j]][3] = True

final_cost = 10000
final_ans = []
for _ in range(300):
    t_order = []
    t_in = {ti: False for ti in t}
    # for ti in t:
    ind = random.sample(range(M), M)
    for i in ind:
        ti = t[i]
        if t_in[ti]:
            continue
        if pre_next[ti][3]:
            continue
        t_order.append(ti)
        while pre_next[ti][2]:
            ti = pre_next[ti][0]
            t_order.append(ti)
            t_in[ti] = True
    keys = set(t_order)
    after = []
    for ti in t:
        if ti in keys:
            continue
        t_order.append(ti)
        after.append(ti)
    after = set(after)

    # print(pre_next, file=sys.stderr)
    # print(len(t_order), t_order, file=sys.stderr)

    cost = 0
    ans = []
    for ti in t_order:
        k = pre_next[ti][1]
        # print(ti, ti[:-k], file=sys.stderr)
        if k > 0 and not ti in after:
            ti = ti[:-k]
        for a in ti:
            i, j, c = nearest[si, sj][a]
            cost += c
            ans.append(f'{i} {j}')
            si, sj = i, j
    score = max(10000-cost, 1001)
    if final_cost > cost:
        final_cost = cost
        final_ans = ans
    # print(f'score: {score}, cost: {cost}', file=sys.stderr)

aa = []
for k, v in pre_next.items():
    aa.append((k, v[1]))
aa = sorted(aa, key=lambda x: x[1], reverse=True)
t_order = []
t_in = {ti: False for ti in t}
# for ti in t:
ind = random.sample(range(M), M)
for ti, _ in aa:
    if t_in[ti]:
        continue
    if pre_next[ti][3]:
        continue
    t_order.append(ti)
    while pre_next[ti][2]:
        ti = pre_next[ti][0]
        t_order.append(ti)
        t_in[ti] = True
keys = set(t_order)
after = []
for ti in t:
    if ti in keys:
        continue
    t_order.append(ti)
    after.append(ti)
after = set(after)

# print(pre_next, file=sys.stderr)
# print(len(t_order), t_order, file=sys.stderr)

cost = 0
ans = []
for ti in t_order:
    k = pre_next[ti][1]
    # print(ti, ti[:-k], file=sys.stderr)
    if k > 0 and not ti in after:
        ti = ti[:-k]
    for a in ti:
        i, j, c = nearest[si, sj][a]
        cost += c
        ans.append(f'{i} {j}')
        si, sj = i, j
score = max(10000-cost, 1001)
if final_cost > cost:
    final_cost = cost
    final_ans = ans

# 解答提出
for a in final_ans:
    print(a)
final_score = max(10000-final_cost, 1001)
# print(f'final score: {final_score}, final cost: {final_cost}', file=sys.stderr)
print(final_score, file=sys.stderr, end='')
