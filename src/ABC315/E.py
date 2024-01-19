import sys

sys.setrecursionlimit(10**6)

N = int(input())
C = []
P = {}
R = [False for _ in range(N)]  # 読んだかどうかフラグ
for i in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    P[i] = tmp[1:]

ans = []

def bfs(i):
    # print('i', i)
    for p in P[i]:
        if R[p-1]:
            continue
        else:
            R[p-1] = True
            bfs(p-1)
            ans.append(p)

bfs(0)

print(' '.join(map(str, ans)))
