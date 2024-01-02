H, W = map(int, input().split())
MOD = 998244353
S = []
for _ in range(H):
    S.append(input())

ans = 1
for k in range(H+W-1):
    cnt_R, cnt_B = 0, 0
    for i in range(k+1):
        j = k-i
        if 0 <= i < H and 0 <= j < W:
            s = S[i][j]
            if s == 'R':
                cnt_R += 1
            elif s == 'B':
                cnt_B += 1
    if cnt_R == 0 and cnt_B == 0:
        ans *= 2
        ans %= MOD
    elif cnt_R > 0 and cnt_B > 0:
        ans = 0
        break
    
print(ans%MOD)
