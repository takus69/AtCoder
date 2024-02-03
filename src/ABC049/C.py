S = input()

c = ['dream', 'erase']
n = ['er', 'r']
nn = ['']
nnn = ''
i = 0
ans = 'YES'
len_S = len(S)
while i < len_S:
    # print(i, S[i:], 'a'+n[-1]+'a')
    if len_S-i == len(nn[-1]):
        if S[i:] == nn[-1]:
            break
    tmp = False
    for ci in range(2):
        cc = c[ci]
        for nnn in nn:
            cc = nnn+cc
            if S[i:i+len(cc)] == cc:
                i += len(cc)
                tmp = True
                nn = ['', n[ci]]
                break
        if tmp:
            break
    if not tmp:
        ans = 'NO'
        break
print(ans)
