N = int(input())
dp = {(-1, 0): 0, (-1, 1): -10**9}
for i in range(N):
    X, Y = map(int, input().split())
    if X == 0:
        dp[(i, 0)] = max(dp[(i-1, 0)]+Y, dp[(i-1, 0)], dp[(i-1, 1)]+Y)
        dp[(i, 1)] = dp[(i-1, 1)]
    else:
        dp[(i, 0)] = dp[(i-1, 0)]
        dp[(i, 1)] = max(dp[(i-1, 0)]+Y, dp[(i-1, 1)])

print(max(dp[(N-1, 0)], dp[(N-1, 1)]))