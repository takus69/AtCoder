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
            print(v, 0)
        else:
            #print('v, i, j, h:', v, i, j, h)
            v2 = b[i][j+1]
            i2 = i
            check = []
            cnt = 0
            for vv in range(v, min(n, v+m-1)):
                if vi[vv] == i:
                    cnt += 1
                check.append(vi[vv])
            check = sorted(check)
            target = []
            for ii in range(m):
                if ii in check:
                    continue
                else:
                    target.append(ii)
            #i_t = random.sample(target, cnt)
            #i2 = i_t[0]
            #while i2 in check:
            #while i2 == i:
            #    i2 = random.randrange(0, m)
            moves = []
            indexs = []
            for jj in range(j, h):
                vv = b[i][jj]
                if vv >= v and vv < v+m:
                    moves.append(vv)
                    indexs.append(jj)
            li = h
            #print(v, b[i], target, moves, indexs)
            #print('before', v, v+m, target, moves, check)
            i_t = random.sample(target, len(moves))
            #print('after', v, moves, i_t, check)
            for ii in range(len(moves)-1, -1, -1):
                ri = indexs[ii]
                rv = moves[ii]
                move_i = i_t[ii]
                ans.append([rv, move_i+1])
                print(rv, move_i+1)
                cost.append(li-ri)
                for vv in b[i][ri:li]:
                    vi[vv] = move_i
                b[move_i] += b[i][ri:li]
                b[i] = b[i][:ri]

                li = ri

            #ans.append([v2, i2+1])
            #print(v2, i2+1)
            ans.append([v, 0])
            b[i] = b[i][:-1]
            print(v, 0)
            #for vv in b[i][j+1:]:
            #    vi[vv] = i2
            #b[i2] += b[i][j+1:]
            #b[i] = b[i][:j]
            #cost.append(h-j)
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
print('#score:', score)

