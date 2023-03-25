S = input()
ans = 0

l = [bin(0)]
for i in range(len(S)):
    s = int(S[i])
    l.append(bin(int(l[i],0) ^ 2**s))

'''
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        if l[i] == l[j]:
            ans += 1
'''
d = {i:0 for i in range(2**10)}
for i in range(len(S)+1):
    k = int(l[i], 0)
    d[k] = d[k] + 1

ans = 0
for k, v in d.items():
    if v >= 2:
        ans += v*(v-1)//2

print(ans)
