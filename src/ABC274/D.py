N, x, y = map(int, input().split())
A = list(map(int, input().split()))

w = 10**4
pre_x = [False for _ in range(2*w+1)]
pre_x[A[0]+w] = True  # x+w
pre_y = [False for _ in range(2*w+1)]
pre_y[w] = True  # y+w

for i in range(1, N):
    tmp = [False for _ in range(2*w+1)]
    if i%2 == 0:  # xの処理
        for j in range(2*w+1):
            if pre_x[j]:
                tmp[j-A[i]] = True
                tmp[j+A[i]] = True
        pre_x = tmp
    else:  # yの処理
        for j in range(2*w+1):
            if pre_y[j]:
                tmp[j-A[i]] = True
                tmp[j+A[i]] = True
        pre_y = tmp

if pre_x[x+w] and pre_y[y+w]:
    print('Yes')
else:
    print('No')
