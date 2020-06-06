N = int(input())
a = []
for i in range(N):
    a.append(input())

shou = N // 2
amari = N % 2
ans = []
for i in range(shou):
    s1 = a[i]
    s2 = a[-i-1]
    flg = False
    for s in s1:
        if s in s2:
            flg = True
            ans.append(s)
            break
    if not flg:
        ans = -1
        break

if isinstance(ans, list):
    ans = ''.join(ans)
    r_ans = ans[::-1]
    if amari == 1:
        ans += a[shou][0]
    ans += r_ans
print(ans)
