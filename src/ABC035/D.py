import heapq

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
root = {i+1: [] for i in range(N)}
root2 = {i+1: [] for i in range(N)}
for _ in range(M):
    a, b, c = map(int, input().split())
    root[a].append((b, c))
    root2[b].append((a, c))
# 行き 
v = [False for _ in range(N)]  # 確定したか
r = [10**9 for _ in range(N)]  # 1からの最短の移動時間
q = []
heapq.heapify(q)
heapq.heappush(q, (0, 1))
r[0] = 0
while len(q) > 0:
    t, a = heapq.heappop(q)
    # print('順番', a)
    if v[a-1]:
        continue
    v[a-1] = True
    for b, c in root[a]:
        if r[b-1] > t+c:
            r[b-1] = t+c
            heapq.heappush(q, (t+c, b))
# 帰り
v2 = [False for _ in range(N)]  # 確定したか
r2 = [10**9 for _ in range(N)]  # 1からの最短の移動時間
q2 = []
heapq.heapify(q2)
heapq.heappush(q2, (0, 1))
r2[0] = 0
while len(q2) > 0:
    t, a = heapq.heappop(q2)
    if v2[a-1]:
        continue
    v2[a-1] = True
    for b, c in root2[a]:
        if r2[b-1] > t+c:
            r2[b-1] = t+c
            heapq.heappush(q2, (t+c, b))

# print(r)
# print(r2)
ans = A[0]*T
for i in range(1, N):
    # print(ans, A[i]*(T-r[i]-r2[i]))
    ans = max(ans, A[i]*(T-r[i]-r2[i]))
print(ans)
