N, K = map(int, input().split())
ab = []
for _ in range(N):
    a, b = map(int, input().split())
    ab.append((a, b))

ab = sorted(ab, key=lambda x: x[0])
now = 0
for a, b in ab:
    now += b
    if now >= K:
        print(a)
        break
