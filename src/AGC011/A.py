N, C, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))
T = sorted(T)

ans = 0
c2 = 0
t2 = 0
for t in T:
    # バスが必要か
    if c2 < 1 or t2 < t:
        ans += 1
        c2 = C
        t2 = t+K
    # 乗客を乗せる
    if t <= t2:
        c2 -= 1
print(ans)
