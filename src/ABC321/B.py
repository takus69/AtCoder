N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
for x in range(101):
    A2 = A + [x]
    max_a, min_a = max(A2), min(A2)
    if sum(A2) - max_a - min_a >= X:
        if ans == -1:
            ans = x
        else:
            ans = min(x, ans)

print(ans)
