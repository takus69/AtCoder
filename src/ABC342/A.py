S = input()
c = {}
for s in S:
    c[s] = c.get(s, 0)+1
for k, v in c.items():
    if v == 1:
        s = k
        break
for i in range(len(S)):
    if S[i] == s:
        ans = i+1
print(ans)
