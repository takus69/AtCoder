N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

def check(i, j):
    ret = True
    for ii in range(i, i+3):
        # print(ii, S[ii][j:j+4])
        if S[ii][j:j+4] != '###.':
            ret = False
            break
    if S[i+3][j:j+4] != '....':
        # print(i+3, S[i+3][j:j+4])
        ret = False
    if S[i+5][j+5:j+9] != '....':
        # print(i+5, S[i+5][j+5:j+9])
        ret = False
    for ii in range(i+6, i+9):
        # print(ii, N)
        # print(ii, S[ii][j+5:j+9])
        if S[ii][j+5:j+9] != '.###':
            ret = False
            break
    return ret

ans = []
for i in range(N-8):
    for j in range(M-8):
        # print('chech', i, j)
        if check(i, j):
            ans.append((i+1, j+1))

# print('ans', ans)
for a in ans:
    print('{} {}'.format(a[0], a[1]))