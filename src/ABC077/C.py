import bisect

N = int(input())
A = map(int, input().split())
B = map(int, input().split())
C = map(int, input().split())
A = sorted(A)
B = sorted(B)
C = sorted(C)

C_cnt = []
for i in range(N):
    bi = B[i]
    j = bisect.bisect_right(C, bi)
    C_cnt.append(N-j)
for i in range(N-2, -1, -1):
    C_cnt[i] += C_cnt[i+1]
ans = 0
for i in range(N):
    ai = A[i]
    j = bisect.bisect_right(B, ai)
    if j < N:
        ans += C_cnt[j]
print(ans)
