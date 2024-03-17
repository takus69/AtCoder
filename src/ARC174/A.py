N, C = map(int, input().split())
A = list(map(int, input().split()))

sum_A = [0]
tmp = 0
for a in A:
    tmp += a
    sum_A.append(tmp)
ans = sum_A[-1]
# print(sum_A)
if C > 0:  # 最大の区間をC倍
    max_lr = 0
    tmp = 0
    for i in range(N):
        a = A[i]
        if tmp+a > 0:
            tmp += a
        else:
            tmp = 0
        if max_lr < tmp:
            max_lr = tmp

    '''
    start_i = N
    for i in range(N):
        if A[i] < 0:
            continue
        else:
            start_i = i
            break
    tmp = sum_A[start_i]
    max_i = start_i
    for i in range(start_i, N+1):
        a = sum_A[i]
        if tmp <= a:
            tmp = a
            max_i = i
    tmp = sum_A[max_i] - sum_A[0]
    for i in range(start_i, max_i):
        a = sum_A[i]
        if tmp < sum_A[max_i] - a:
            tmp = sum_A[max_i] - a
    '''
    ans = max(ans, ans+(C-1)*max_lr)
else:  # 最小の区間をC倍
    min_lr = 0
    tmp = 0
    for i in range(N):
        a = A[i]
        if tmp+a < 0:
            tmp += a
        else:
            tmp = 0
        if min_lr > tmp:
            min_lr = tmp
    
    '''
    start_i = N
    for i in range(N):
        if A[i] > 0:
            continue
        else:
            start_i = i
            break
    tmp = sum_A[start_i]
    min_i = start_i
    for i in range(start_i, N+1):
        a = sum_A[i]
        if tmp >= a:
            tmp = a
            min_i = i
    tmp = sum_A[min_i] - sum_A[0]
    for i in range(start_i, min_i):
        a = sum_A[i]
        if tmp > sum_A[min_i] - a:
            tmp = sum_A[min_i] - a
    '''
    ans = max(ans, ans+(C-1)*min_lr)
print(ans)
