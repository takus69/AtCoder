N, Q = map(int, input().split())
T, A, B = [], [], []
for i in range(Q):
    t, a, b = map(int, input().split())
    T.append(t)
    A.append(a)
    B.append(b)

follow = {}
for i in range(Q):
    t = T[i]
    a = A[i]
    b = B[i]
    if t == 1:
        f = follow.get(a, {})
        f[b] = 1
        follow[a] = f
    elif t == 2:
        f = follow.get(a, {})
        f[b] = 0
        follow[a] = f
    else:
        if a in follow.keys():
            if b in follow[a].keys():
                if b in follow.keys():
                    if a in follow[b].keys():
                        if follow[a][b] == 1 and follow[b][a] == 1:
                            print('Yes')
                            continue
        print('No')
