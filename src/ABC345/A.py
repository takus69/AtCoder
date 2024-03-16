S = input()

ans = 'Yes'
if S[0] == '<' and S[-1] == '>':
    ans = 'Yes'
    for s in S[1:-1]:
        if s == '=':
            continue
        else:
            ans = 'No'
            break
else:
    ans = 'No'
print(ans)
