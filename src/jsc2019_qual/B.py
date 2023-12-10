# A内の転倒数×K + Aともう一つのAに対する転倒数×(1/2)(K-1)K

N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7
tmp1 = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            tmp1 += 1

tmp2 = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            tmp2 += 1

ans = tmp1*K+(tmp2)*K*(K-1)//2
ans %= mod
print(ans)
