import queue

N, M = map(int, input().split())
l, d, k, c, A, B = [], [], [], [], [], []
Edge = {}
Train = {}
for _ in range(M):
    ll, dd, kk, cc, AA, BB = map(int, input().split())
    l.append(ll)
    d.append(dd)
    k.append(kk)
    c.append(cc)
    A.append(AA)
    B.append(BB)
    tmp = Edge.get(BB, [])
    tmp.append(AA)
    Edge[BB] = tmp
    Train[(AA, BB)] = [ll, dd, kk, cc]

ans = ['Unreachable']*N
ans[-1] = 3*(10**18)
c = [False]*N
q = queue.Queue()
q.put(N)

def check(AA, BB, tt):
    # AAからBBにttに着く最大のtを返す
    ll, dd, kk, cc = Train[(AA, BB)]
    k = (tt-ll-cc)/dd
    if k >= 0:
        t = ll + (dd*min(int(k), kk-1))
        print(ll, dd, int(k), kk, cc)
    else:
        t = 'Unreachable'
    return t

while not q.empty():
    BB = q.get()
    if BB in Edge.keys():
        e = Edge[BB]
    else:
        continue
    tt = ans[BB-1]
    # print('BB', BB, 'tt', tt)
    for AA in e:
        if not c[AA-1]:
            q.put(AA)
        c[AA-1] = True
        if tt == 'Unreachable':
            continue
        else:
            t = check(AA, BB, tt)
        print('AA', AA, 'BB', BB, 't', t)
        if ans[AA-1] == 'Unreachable':
            ans[AA-1] = t
        else:
            if t != 'Unreachable':
                ans[AA-1] = max(ans[AA-1], t)
for i in range(N-1):
    print(ans[i])
