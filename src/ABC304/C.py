N, D = map(int, input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

t = [0]
ans = [True] + [False]*(N-1)
i = 0
cnt = 1

while True:
    # print(i, ans, t)
    tt = t[i]
    tx, ty = X[tt], Y[tt]
    for j in range(N):
        if ans[j]:
            continue
        else:
            # print(j, tx, ty, X[j], Y[j], ((tx-X[j])**2 + (ty-Y[j])**2)**(1/2), D)
            if D >= ((tx-X[j])**2 + (ty-Y[j])**2)**(1/2):
                ans[j] = True
                t.append(j)
                cnt += 1
    i += 1
    if i >= cnt:
        break

for a in ans:
    if a:
        print('Yes')
    else:
        print('No')
