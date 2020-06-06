N, M, Q = map(int, input().split())
u = []
v = []
for i in range(M):
    t_u, t_v = map(int, input().split())
    u.append(t_u - 1)
    v.append(t_v - 1)
c = list(map(int, input().split()))
s = []
for i in range(Q):
    s.append(input())

v_side = {i: [] for i in range(N)}
for i in range(M):
    t_u = u[i]
    t_v = v[i]
    v_side[t_u].append(t_v)
    v_side[t_v].append(t_u)

ans = []
for i in range(Q):
    q = list(map(int, s[i].split()))
    if q[0] == 1:
        x = q[1] - 1
        ans.append(c[x])
        for x2 in v_side[x]:
            c[x2] = c[x]
    else:
        x = q[1] - 1
        y = q[2]
        ans.append(c[x])
        c[x] = y

for a in ans:
    print(a)
