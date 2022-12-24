S = input()
i = len(S)-1
cnt = 0
while(i >= 0):
    if i >= 2:
        if S[i-1]+S[i] == '00':
            cnt += 1
            i -= 2
            continue
        else:
            cnt += 1
            i -= 1
    else:
        cnt += 1
        i -= 1
print(cnt)
    