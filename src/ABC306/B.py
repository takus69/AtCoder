A = list(map(int, input().split()))

ans = 0
for i in range(len(A)):
    a = A[i]
    ans += a*2**i
print(ans)
