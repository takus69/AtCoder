N = int(input())
sc = {}
sum_c = 0
for _ in range(N):
    s, c = map(int, input().split())
    sc[s] = c
    sum_c += c
sc2 = sorted(sc.items())

for s, c in sc2:
    s2 = s
    c2 = sc[s]
    while c2 > 1:
        if s2 in sc.keys():
            sc[s2] -= c2
        else:
             sc[s2] = 0
        if c2 % 2 == 1:
            sc[s2] += 1
        s2 *= 2
        c2 //= 2
        if s2 in sc.keys():
            sc[s2] += c2
        else:
            sc[s2] = c2
        sum_c -= c2
        c2 = sc[s2]
        # print(sc)
print(sum_c)