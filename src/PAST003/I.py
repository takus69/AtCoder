N = int(input())
Q = int(input())
row = {i: i for i in range(N)}
col = {i: i for i in range(N)}
t_cnt = 0
ans = []
for _ in range(Q):
    query = input()
    if query == '3':
        t_cnt += 1
    else:
        q, a, b = map(int, query.split())
        a -= 1
        b -= 1
        if q == 1:
            if t_cnt % 2 == 0:
                row[a], row[b] = row[b], row[a]
            else:
                col[a], col[b] = col[b], col[a]
        if q == 2:
            if t_cnt % 2 == 0:
                col[a], col[b] = col[b], col[a]
            else:
                row[a], row[b] = row[b], row[a]
        if q == 4:
            if t_cnt % 2 == 0:
                ans.append(N*row[a] + col[b])
            else:
                ans.append(N*row[b] + col[a])
    # print(query, row, col)

for a in ans:
    print(a)
