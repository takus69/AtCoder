N = int(input())

ans = [[-1 for _ in range(N)] for _ in range(N)]
tx, ty = (N+1)//2-1, (N+1)//2-1
ans[ty][tx] = 'T'
x, y = tx, ty-1
mx, my = 1, 0
for i in range(1, N**2):
    # print(ans, x, y)
    ans[y][x] = i
    x += mx
    y += my
    if x-tx == ty-y and x-tx > 0:
        mx, my = 0, 1
    elif x == y and x-tx > 0:
        mx, my = -1, 0
    elif tx-x == y-ty and tx-x > 0:
        mx, my = 0, -1
    elif tx-x == ty-y-1 and tx-x > 0:
        mx, my = 1, 0

for a in ans:
    print(' '.join(map(str, a)))
