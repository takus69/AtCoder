H, W, N = map(int, input().split())
T = input()
S = []
for _ in range(H):
    S.append(input())
S2 = [[] for _ in range(H)]
for i in range(H):
    tmp = 0
    for j in range(W):
        if S[i][j] == '#':
            tmp += 1
        S2[i].append(tmp)

p = [[0, 0]]
for t in T:
    if t == 'L':
        p.append([p[-1][0], p[-1][1]-1])
    elif t == 'R':
        p.append([p[-1][0], p[-1][1]+1])
    elif t == 'U':
        p.append([p[-1][0]-1, p[-1][1]])
    else:
        p.append([p[-1][0]+1, p[-1][1]])

min_i, min_j = 500, 500
max_i, max_j = -500, -500
for i, j in p:
    min_i, min_j = min(i, min_i), min(j, min_j)
    max_i, max_j = max(i, max_i), max(j, max_j)

ans = 0
for i in range(max(1, 1-min_i), min(H-1, H-1-max_i)):
    for j in range(max(1, 1-min_j), min(W-1, W-1-max_j)):
        flg = True
        for (i2, j2) in p:
            if S[i+i2][j+j2] == '#':
                flg = False
                break
        if flg:
            ans += 1

'''
for i in range(len(T)+1):
    p[i][0] -= min_i
    p[i][1] -= min_j
max_h = 0
max_w = 0
for i, j in p:
    max_h = max(max_h, i)
    max_w = max(max_w, j)
max_h += 1
max_w += 1
c = [[500, -500] for _ in range(max_h)]
for h in range(max_h):
    for i, j in p:
        if i == h:
            c[h][0] = min(c[h][0], j)
            c[h][1] = max(c[h][1], j)
ans = 0
for i in range(1, H-max_h):
    for j in range(1, W-max_w):
        flg = True
        for h in range(max_h):
            if S2[i+h][j+c[h][0]-1] == S2[i+h][j+c[h][1]]:
                continue
            else:
                flg = False
                break
        if flg:
            ans += 1
'''
print(ans)
