N = int(input())
A = list(map(int, input().split()))
Q = int (input())
ans = []
flag1 = False
x1 = None
x2 = {}
for i in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        x = query[1]
        x1 = x
        x2 = {}
        flag1 = True
    elif q == 2:
        i = query[1]
        x = query[2]
        if flag1:
            x2[i-1] = x2.get(i-1, 0) + x
        else:
            A[i-1] += x
    else:
        i = query[1]
        if flag1:
            ans.append(x1+x2.get(i-1, 0))
        else:
            ans.append(A[i-1])
for a in ans:
    print(a)
