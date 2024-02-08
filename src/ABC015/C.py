import itertools

N, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(list(map(int, input().split())))

ans = 'Nothing'
for p in itertools.product(range(K), repeat=N):
    tmp = 0
    for i in range(N):
        tmp ^= T[i][p[i]]
    if tmp == 0:
        ans = 'Found'
        break
print(ans)
