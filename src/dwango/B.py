S = input()

cnt = 0
ans = 0
flg2 = False
for s in S:
    # print(s, flg2, cnt, ans)
    if s == '2':
        if flg2:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
            flg2 = False
        flg2 = True
    elif s == '5' and flg2:
        cnt += 1
        flg2 = False
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 0
        flg2 = False
ans += cnt * (cnt + 1) // 2

print(ans)
