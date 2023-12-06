N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
for bi in b:
    c.append(a[0] ^ bi)
c = set(c)
b = sorted(b)
ans = []
for x in c:
    b2 = []
    for ai in a:
        b2.append(ai ^ x)
    b2 = sorted(b2)
    flag = True
    for i in range(N):
        if b[i] != b2[i]:
            flag = False
            break
    if flag:
        ans.append(x)

ans = sorted(ans)
print(len(ans))
for x in ans:
    print(x)