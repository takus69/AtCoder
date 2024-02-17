from math import lcm

N, M, K = map(int, input().split())
lo, hi = 0, 10**18
while lo + 1 < hi:
    mi = (lo + hi) // 2
    c = mi//N + mi//M - mi//lcm(N, M) * 2
    if c < K:
        lo = mi
    else:
        hi = mi
print(hi)

'''
a = K//(N+M-2)
cnt = a*(N+M-2)  # aMNまでの個数
b = K%(N+M-2)  # aMN以降で必要な個数
bN = b*M//(M+N)  # Nの倍数で必要な個数
bM = b*N//(M+N)  # Mの倍数で必要な個数
cnt += bN
cnt += bM
ans = a*M*N
while cnt < K:
    if bN*N < bM*M:
        bN += 1
        cnt += 1
    else:
        bM += 1
        cnt += 1
ans += max(bN*N, bM*M)
if min(N, M) == 1:
    b = max(N, M)
    a = (K*b)//(b-1)
    cnt = a - a//b
    ans = a
    if ans % K == 0:
        ans -= 1
    while cnt < K:
        ans += 1
        if ans % K == 0:
            ans += 1
        cnt += 1

# print(a*(N+M-2), b, bN, bM)
print(ans)
'''
