S = input()
dic = {'a': 0, 'b': 0, 'c': 0}
for s in S:
    dic[s] += 1
n = len(S)
ans = 'YES'
for v in dic.values():
    if v != n//3 and v != n//3+1:
        ans = 'NO'
print(ans)
