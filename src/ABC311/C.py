N = int(input())
A = list(map(int, input().split()))
C = {i+1: 0 for i in range(N)}

start = None
ans = []
for i in range(N):
    flg = False
    if C[i+1] == 0:
        C[i+1] = 1
        starts = {i+1: 1}
        ans.append(i+1)
        a = A[i]
        ans.append(a)
        while True:
            if C[a] == 1:
                if a in starts.keys():
                    start = a
                    flg = True
                break
            else:
                C[a] = 1
                starts[a] = 1
                a = A[a-1]
                ans.append(a)
    if flg:
        break
ans2 = []
flg = False
for a in ans:
    if flg:
        ans2.append(a)
    else:
        if a == start:
            flg = True
print(len(ans2))
print(' '.join(list(map(str, ans2))))
