N = int(input())
S = input()

flg = False
ans = 'out'
for s in S:
    if flg:
        if s == '*':
            ans = 'in'
        elif s == '|':
            flg = False
    else:
        if s == '|':
            flg = True
print(ans)
