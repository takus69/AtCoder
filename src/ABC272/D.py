import queue

N, M = map(int, input().split())
moves = []

for i in range(-N-1, N):
    for j in range(-N-1, N):
        # print(i, j)
        if (i+1)**2 + (j+1)**2  == M:
            moves.append((i+1, j+1))
info = {(i, j): [False, -1] for i in range(1, N+1) for j in range(1, N+1)}  # [訪問したか, 訪問の最小回数]

q = queue.Queue()
q.put((1, 1))
info[(1, 1)][0] = True
info[(1, 1)][1] = 0
while not q.empty():
    i, j = q.get()
    # print('(i, j):', i, j)
    cnt = info[(i, j)][1]
    for move in moves:
        i2, j2 = i + move[0], j + move[1]
        if 1 <= i2 <= N and 1 <= j2 <= N:
            if not info[(i2, j2)][0]:
                q.put((i2, j2))
                info[(i2, j2)][0] = True
                info[(i2, j2)][1] = cnt + 1

for i in range(1, N+1):
    ans = ''
    for j in range(1, N+1):
        ans += str(info[(i, j)][1]) + ' '
    print(ans[:-1])
