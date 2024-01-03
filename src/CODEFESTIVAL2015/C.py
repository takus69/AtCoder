N, K, M, R = map(int, input().split())
S = []
for _ in range(N-1):
    S.append(int(input()))

S = sorted(S, reverse=True)
next = 0
for s in S[:K]:
    next += R - s
if K < N:
    next += S[K-1]
else:
    next += R

ans = 0
if next > M:
    ans = -1
elif K == N:
    ans = max(next, 0)
elif next > S[K-1]:
    ans = next
print(ans)
