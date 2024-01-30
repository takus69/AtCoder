s = input()

ans = 0
cnt = 0
i = len(s)
while i > 2:
    tmp = s[i-3:i]
    if tmp == 'ABC':
        cnt += 1
        ans += cnt
        i -= 3
        # print(i, 'ABC', ans)
        while True:
            if i-1 < 0:
                break
            if s[i-1] == 'A':
                ans += cnt
                # print(i, 'AA', ans)
                i -= 1
            else:
                break
    elif tmp[1:] == 'BC':
        cnt += 1
        i -= 2
    else:
        flg = False
        cnt = 0
        i -= 1
print(ans)
