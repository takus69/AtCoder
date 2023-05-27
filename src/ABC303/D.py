X, Y, Z = map(int, input().split())
S = input()

dp = {}
dp[(0, 0)] = 0
dp[(0, 1)] = Z
for i in range(1, len(S)+1):
    s = S[i-1]
    if s == 'A':
        caps = 1
        not_caps = 0
    else:
        caps = 0
        not_caps = 1
    dp[(i, caps)] = min(dp[(i-1, caps)]+X, dp[(i-1, not_caps)]+Z+X)
    dp[(i, not_caps)] = min(dp[(i-1, not_caps)]+Y, dp[(i-1, caps)]+Z+Y)
#print(dp)
print(min(dp[(len(S), 0)], dp[(len(S), 1)]))