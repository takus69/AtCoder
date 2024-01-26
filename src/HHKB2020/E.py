H, W = map(int, input().split())
S = []

MOD = 1000000007 

L = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(2)] # 照らされる照明が置ける箇所の数
# 横方向の照らされる照明の置ける箇所の数を数える
cnt = 0
for i in range(H):
    S.append(input())
    c = 0
    for j in range(W):
        if S[i][j] == '.':
            cnt += 1
            c += 1
            L[0][i][j] = c
        else:
            c = 0
    c = 0
    for j in range(W-1, -1, -1):
        if S[i][j] == '.':
            if c == 0:
                c = L[0][i][j]
            L[0][i][j] = c
        else:
            c = 0

# 縦方向の照らされる照明の置ける箇所の数を数える
for j in range(W):
    c = 0
    for i in range(H):
        if S[i][j] == '.':
            c += 1
            L[1][i][j] = c
        else:
            c = 0
    c = 0
    for i in range(H-1, -1, -1):
        if S[i][j] == '.':
            if c == 0:
                c = L[1][i][j]
            L[1][i][j] = c
        else:
            c = 0

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            # ans += ((pow(2, L[0][i][j]+L[1][i][j]-1)-1)%MOD) * (pow(2, cnt-L[0][i][j]-L[1][i][j]+1, MOD))
            ans += pow(2, cnt, MOD)
            ans -= pow(2, cnt-L[0][i][j]-L[1][i][j]+1, MOD)
            ans %= MOD
# print(L)
# print(L2)
print(ans)
