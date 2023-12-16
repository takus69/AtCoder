import queue

N, M = map(int, input().split())
AB = {i: [] for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    AB[A].append(B)
    AB[B].append(A)
info = {i: [False, 0, 0] for i in range(1, N+1)}  # [訪問したかどうか、1への最小の移動回数、道しるべ]

q = queue.Queue()
q.put(1)
info[1][0] = True
info[1][1] = 0

while not q.empty():
    i = q.get()
    # print('i:', i)
    now = info[i][1]
    for j in AB[i]:
        if not info[j][0]:
            # print('j:', j)
            q.put(j)
            info[j][1] = now + 1
            info[j][2] = i
            info[j][0] = True
        # print(info)

print('Yes')
for i in range(2, N+1):
    print(info[i][2])
