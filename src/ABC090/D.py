N, K = map(int, input().split())
ans = 0
if K == 0:
    ans = N*N
else:
    for b in range(K+1, N+1):
        ans += (N//b)*(b-K)
        if N%b >= K:
            ans += N%b-K+1
        # print(b, ans)
print(ans)
