N = int(input())
S = input()

ans = -1
t = 0
flg = False
for s in S:
    #print(s)
    if flg:
        if s == 'o':
            t += 1
            ans = max(t, ans)
        else:
            t = 0
    else:
        if s == '-':
            flg = True
t = 0
flg = False
for s in S[-1::-1]:
    #print(s)
    if flg:
        if s == 'o':
            t += 1
            ans = max(t, ans)
        else:
            t = 0
    else:
        if s == '-':
            flg = True
print(ans)