# A内の転倒数×K + Aともう一つのAに対する転倒数×(1/2)(K-1)K

N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7
ans = 0
# tmp1 = 0
for i in range(N):
    tmp1 = 0
    for j in range(i, N):
        if A[i] > A[j]:
            tmp1 += 1
            # tmp1 %= mod

    tmp2 = 0
#for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            tmp2 += 1
            # tmp2 %= mod

# print(tmp1, tmp2)
    #ans += (tmp1 * K) + ((tmp1+tmp2) * (K-1)*K)//2
    ans += tmp1*K+(tmp2)*K*(K-1)//2
    #ans = int(ans)
    ans %= mod
print(ans)
