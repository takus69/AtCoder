N = int(input())
A = list(map(int, input().split()))

d = {i:0 for i in range(N+1)}
ans = []
for a in A:
    d[a] += 1
    if d[a] == 2:
        ans.append(a)

print(' '.join(map(str, ans)))