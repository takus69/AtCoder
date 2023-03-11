N, M = map(int, input().split())
A, B, C, D = [], [], [], []
for _ in range(M):
    a, b, c, d = input().split()
    A.append(int(a))
    B.append(b)
    C.append(int(c))
    D.append(d)

d = {}
for i in range(N):
    d[(i+1, 'R')] = (i+1, 'B')
    d[(i+1, 'B')] = (i+1, 'R')

for i in range(M):
    p1 = (A[i], B[i])
    p2 = (C[i], D[i])
    if p1 == d[p2] and p2 == d[p1]:
        d[p1] = d[p2]
        d.pop(p2)
    else:
        d[d[p1]] = d[p2]
        d[d[p2]] = d[p1]
        d.pop(p1)
        d.pop(p2)

n1, n2 = 0, 0
for k in d.keys():
    if k == d[k]:
        n1 += 1
    else:
        n2 += 1

print(n1, n2//2)
