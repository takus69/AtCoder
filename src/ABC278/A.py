N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = A[K:]+[0]*K
if len(ans) > N:
    ans = ans[:N]
print(' '.join(map(str, ans)))