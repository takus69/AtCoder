N = int(input())
A = list(map(int, input().split()))
ans = 0
MOD = 998244353
N1, N2 = 1, 1
for i in range(N):
    if i == 0:
        N1 = 1
    else:
        N1 *= 1+N
        N1 %= MOD
    N2 *= N
    N2 %= MOD
    a = A[i] % MOD

    # print(i, N, A[i], (1+N)**i, N**(i+1))
    ans += a * N1 * pow(N2, -1, MOD)
ans %= MOD
print(ans)
