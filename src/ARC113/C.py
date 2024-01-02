S = input()
ans = 0
pre = {S[-1]: 1}
pre_s = None
pre_i = None
n = len(S)
flg = True
for i in range(n-2, -1, -1):
    s = S[i]
    pre[s] = pre.get(s, 0)+1
    if s != pre_s:
        flg = True
    if s == S[i+1] and flg:
        if s != pre_s:
            ans += n-(i+2)-(pre[s]-2)
        else:
            ans += pre_i-(i+2)-(pre[s]-2)
        # print(s, n, i, ans, pre[s], pre_s)
        pre = {}
        pre_s = s
        pre_i = i
        flg = False
print(ans)
