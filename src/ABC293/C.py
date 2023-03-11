import queue
import copy

H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

roots = [[[(1,1)]]]
for i in range(H+W-2):
    roots.append([])
    for r in roots[i]:
        #print(r[-1])
        #r = copy.deepcopy(rr)
        h, w = r[-1][0], r[-1][1]
        if h+1 <= H:
            roots[i+1].append(r+[(h+1, w)])
        if w+1 <= W:
            roots[i+1].append(r+[(h, w+1)])
        #print(roots)

ans = 0

for r in roots[-1]:
    l = []
    flg = True
    for p in r:
        h, w = p[0], p[1]
        a = A[h-1][w-1]
        if a in l:
            flg = False
            #break
        else:
            l.append(a)
    #print(flg, r, l)
    if flg:
        ans += 1

print(ans)
