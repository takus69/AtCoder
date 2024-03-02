N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    ans = []
    for j in range(N):
        if A[i][j] == 1:
            ans.append(j+1)
    print(' '.join(map(str, ans)))
