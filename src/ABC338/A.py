S = input()

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 'Yes'
for i in range(len(S)):
    if i == 0:
        if S[i] in ABC:
            continue
        else:
            ans = 'No'
            break
    else:
        if S[i] in ABC:
            ans = 'No'
            break

print(ans)    
