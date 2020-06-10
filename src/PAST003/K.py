N, Q = map(int, input().split())

# コンテナci, テーブルti
# コンテナiの下にあるもの
ci = {i: 't{}'.format(i) for i in range(1, N+1)}
# テーブルiの一番上のコンテナ番号
ti = {i: i for i in range(1, N+1)}

for _ in range(Q):
    f, t, x = map(int, input().split())
    tmp_ti_f = ti[f]
    if ci[x].startswith('t'):
        ti[f] = 0
    else:
        ti[f] = int(ci[x][1:])
    if ti[t] == 0:
        ci[x] = 't{}'.format(t)
    else:
        ci[x] = 'c{}'.format(ti[t])
    ti[t] = tmp_ti_f

ans = {}
for i in range(1, N+1):
    j = ti[i]
    if j == 0:
        continue
    ans[j] = i
    while ci[j].startswith('c'):
        j = int(ci[j][1:])
        ans[j] = i

for i in range(1, N+1):
    print(ans[i])
