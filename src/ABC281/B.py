S = input()

for i in range(len(S)):
    ret = 'No'
    if len(S) == 8:
        if S[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if S[-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                try:
                    num = int(S[1:-1])
                    if num >= 100000 and num <= 999999:
                        ret = 'Yes'
                except:
                    None
print(ret)