N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
K = min(K, N-K+1)
for i in range(N):
    if i < K:
        ans += a[i]*(i+1)
    elif N-1-i < K:
        ans += a[i]*(N-i)
    else:
        ans += a[i]*K
print(ans)
