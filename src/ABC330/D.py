N = int(input())
S = []
for _ in range(N):
    S.append(input())

row_cnt = []
for i in range(N):
    cnt = 0
    for s in S[i]:
        if s == 'o':
            cnt += 1
    row_cnt.append(cnt)

col_cnt = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if S[j][i] == 'o':
            cnt += 1
    col_cnt.append(cnt)
# print(row_cnt, col_cnt)
ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            ans += (row_cnt[i]-1)*(col_cnt[j]-1)
            # print(i, j, (row_cnt[i]-1)*(col_cnt[j]-1))

print(ans)
