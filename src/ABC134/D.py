N = int(input())
a = list(map(int, input().split()))

b = [0 for _ in range(N)]
for i in range(N, 0, -1):
    ai = a[i-1]
    for j in range(N//i, 1, -1):
        k = i*j-1
        b[i-1] = (b[i-1]+b[k])%2
    if b[i-1] == ai:
        b[i-1] = 0
    else:
        b[i-1] = 1

ans = []
for i in range(N):
    if b[i] == 1:
        ans.append(i+1)

print(len(ans))
if len(ans) > 0:
    print(' '.join(map(str, ans)))
