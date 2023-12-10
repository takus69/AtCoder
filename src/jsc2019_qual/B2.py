N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7
ans = 0

for i in range(N):
    tmp1 = 0
    for j in range(i+1, N):
        if A[i] > A[j]:
            tmp1 += 1


    tmp2 = 0

    for j in range(i):
        if A[i] > A[j]:
            tmp2 += 1



    print(i, tmp1, tmp2)
    ans += tmp1*K+(tmp1+tmp2)*K*(K-1)//2
    # print(ans)
    ans %= mod
print(ans)