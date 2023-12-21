N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

ans = 0

pre = 0
for i in range(N):
    ai = A[i] % 998244353
    ans += ai*ai
    ans += ai*pre
    pre = (2*pre + ai) % 998244353
    ans %= 998244353

print(ans)
