N, D = map(int, input().split())

max_ND = N*(N-1)//2
if N*D > max_ND:
    print('No')
else:
    print('Yes')
    cnt = 0
    d = 1
    i = 0
    for i in range(N):
        for j in range(D):
            print(i+1, (i+j+1)%N+1)
