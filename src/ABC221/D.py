N = int(input())
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, 1))
    AB.append((A+B, -1))
AB = sorted(AB, key=lambda x: x[0])
X = []
for ab, _ in AB:
    X.append(ab)
X = set(X)
AB2 = {x: 0 for x in X}
for x, c in AB:
    AB2[x] += c

ans = [0 for _ in range(N+1)]
num = 0
pre_x = 0
for x, c in AB2.items():
    ans[num] += x - pre_x
    num += c
    pre_x = x
print(' '.join(map(str, ans[1:])))
