C = int(input())
N, M, L = 0, 0, 0
for _ in range(C):
    N2, M2, L2 = sorted(map(int, input().split()))
    N = max(N2, N)
    M = max(M2, M)
    L = max(L2, L)

print(N*M*L)
