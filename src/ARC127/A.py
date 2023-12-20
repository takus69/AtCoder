N = input()
'''
2xxx: 1000個
1xxx: xxx+1個

12xx: 100個
11xx: xx+1個
01xx: 100個
'''

ans = 0
# 先頭が0の場合の数
for i in range(1, len(N)):
    ans += 10**(len(N)-i-1)*i
    # print('ans', ans)
# 先頭が1の場合の数
t_max = int(N[0])
for i in range(len(N)):
    t = int(N[i])
    if t_max > 1 or t > 1:
        ans += 10**(len(N)-i-1)
    elif t == 1:
        if len(N[(i+1):]) > 0:
            ans += int(N[(i+1):])+1
        else:
            ans += 1
    else:
        break
    t_max = max(t, t_max)
    # print('ans', ans)

print(ans)
