N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
ans = 1
tmp = 1
l = 0
r = 0
while True:
    if A[r] - A[l] < M:
        r += 1
        if r >= N:
            break
    else:
        l += 1
        tmp -= 1
    if A[r] - A[l] < M:
        tmp += 1
        ans = max(tmp, ans)
print(ans)
