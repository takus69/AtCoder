T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    b = s - a
    if b < 0:
        ans = 'No'
    elif a & b == a:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
    '''
    ans = 'Yes'
    a = bin(a)[2:]
    b = bin(b)[2:]
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    for i in range(n):
        if b[i] == '0' and a[i] == '1':
            ans = 'No'
    print(ans)
    '''