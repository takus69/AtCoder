import queue

N, M = map(int, input().split())
G = {i: [] for i in range(N)}
E = {}
for _ in range(M):
    A, B, X, Y = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
    E[(A-1, B-1)] = (X, Y)
    E[(B-1, A-1)] = (-X, -Y)
# print('G:', G, 'E:', E)
ans = [['undecidable', False] for _ in range(N)]
ans[0] = [0, 0, True]
q = queue.Queue()
for B in G[0]:
    q.put((0, B))
while not q.empty():
    A, B = q.get()
    X, Y = E[(A, B)]
    XY = ans[A]
    XA, YA = XY[0], XY[1]
    ans[B] = [XA+X, YA+Y, True]
    for B2 in G[B]:
        if not ans[B2][-1]:
            q.put((B, B2))
# print(ans)
for XY in ans:
    if XY[-1]:
        print(f'{XY[0]} {XY[1]}')
    else:
        print(XY[0])
