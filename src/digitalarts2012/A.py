s = input().split()
N = int(input())
t = [input() for _ in range(N)]

for i in range(len(s)):
    si = s[i]
    for ti in t:
        flag = True
        if len(si) == len(ti):
            for j in range(len(si)):
                if si[j] != ti[j] and ti[j] != '*':
                    flag = False
                    break
            if flag:
                s[i] = '*'*len(si)

print(' '.join(s))
