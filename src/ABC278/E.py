H, W, N, h, w = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

hh = [0]*w
for i in range(w):
    for j in range(h):
        hh[i] += A[j][i]
print('hh', hh)
ans = [[0]*(W-w+1)]*(H-h+1)
for i in range(H-h+1):
    if i == 0:
        None
    else:
        # hhをupdate
        for kk in range(w):
            hh[kk] = hh[kk] - A[i-1][kk] + A[i+h][kk]
    for j in range(W-w+1):
        for k in range(w):
            ans[i][j] += hh[k]
print(ans)
for a in ans:
    print(' '.join(map(str, a)))