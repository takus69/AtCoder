N = int(input())
A = list(map(int, input().split()))

min_a = abs(A[0])
cnt_minus = 0
ans = 0
for a in A:
    if a < 0:
        cnt_minus += 1
    min_a = min(abs(a), min_a)
    ans += abs(a)

if cnt_minus % 2 == 1:
    ans -= min_a*2

print(ans)
