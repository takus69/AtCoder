import copy
import random


n, m = map(int, input().split())
b = {}
for i in range(m):
    b[i] = list(map(int, input().split()))

vi = {}
for i in range(m):
    for v in b[i]:
        vi[v] = i

def make_ans(n, m, b, vi):
    ans = []
    cost = []
    for v in range(1, n+1):
        i = vi[v]
        h = len(b[i])
        for j in range(h):
            v2 = b[i][j]
            if v2 == v:
                break
        if j+1 == h:
            ans.append([v, 0])
            b[i] = b[i][:-1]
            #print(v, 0)
        else:
            #print('i, j:', i, j)
            v2 = b[i][j+1]
            i2 = i
            while i == i2:
                i2 = random.randrange(0, m)
            ans.append([v2, i2+1])
            #print(v2, i2+1)
            ans.append([v, 0])
            #print(v, 0)
            for vv in b[i][j+1:]:
                vi[vv] = i2
            b[i2] += b[i][j+1:]
            b[i] = b[i][:j]
            cost.append(h-j)
    return ans, sum(cost)

score = 0
ans = None
for _ in range(1000):
    tmp_ans, tmp_cost = make_ans(n, m, copy.deepcopy(b), copy.deepcopy(vi))
    tmp_score = max(1, 10000 - tmp_cost)
    if tmp_score > score:
        ans = tmp_ans
        score = tmp_score

for a in ans:
    print('{} {}'.format(a[0], a[1]))
#print('#score:', score)

