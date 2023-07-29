N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B)

def check_b(a):
    l, r = 0, M-1
    if B[r] >= a:
        ret = 1
    else:
        ret = 0
    while True:
        flg = False
        m = (l+r)//2
        # print('check', a, l, m , r, B[m], ret)
        if m == l:
            flg = True
        if B[m] >= a:
            r = m
            ret = M-r
        else:
            l = m
        if flg:
            break
    # print('ret', ret)
    return ret

def check_a(a):
    l, r = 0, N-1
    if A[r] <= a:
        ret = N
        return ret
    else:
        ret = 0
    while True:
        flg = False
        m = (l+r)//2
        if m == l:
            flg = True
        if A[m] > a:
            r = m
        else:
            l = m
            ret = l+1
        if flg:
            break
    # print('ret', ret)
    return ret

ans = B[M-1]+1
target = A + [b+1 for b in B]
target = sorted(target)
for t in target:
    n_a = check_a(t)
    n_b = check_b(t)
    # print(t, n_a, n_b)
    if n_a >= n_b:
        ans = t
        break
'''
for i in range(N):
    n_b, b = check(A[i])
    # print(A[i], i+1, n_b)
    if n_b == 0:
        ans = min(ans, B[M-1]+1)
    elif n_b > i+1:
        ans = min(ans, B[M-1]+1)
    elif i+1 >= n_b:
        ans = min(ans, A[i])
'''
print(ans)
