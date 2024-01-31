import itertools

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = [0] + list(itertools.accumulate(A))
sum_B = [0] + list(itertools.accumulate(B))

i, j = N, 0
ans = 0
while i > -1 and j <= M:
    if sum_A[i]+sum_B[j] <= K:
        ans = max(ans, i+j)
        j += 1
    else:
        i -= 1
print(ans)
