N, Q = map(int, input().split())
P = []
for _ in range(N):
    P.append(input())

# 累積和を求める
cnt_b = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        pre_cnt = 0
        if i-1 >= 0 and j-1 >=0:
            pre_cnt += cnt_b[i-1][j] + cnt_b[i][j-1] - cnt_b[i-1][j-1]
        elif i-1 >= 0:
            pre_cnt += cnt_b[i-1][j]
        elif j-1 >= 0:
            pre_cnt += cnt_b[i][j-1]
        if P[i][j] == 'B':
            cnt_b[i][j] = pre_cnt + 1
        else:
            cnt_b[i][j] = pre_cnt
# print(cnt_b)

def sum_b(i, j):
    # (i, j)までの累積和を求める
    ret = 0
    i1, i2 = (i+1)//N, (i+1)%N
    j1, j2 = (j+1)//N, (j+1)%N
    # print('sum_b', i, j, i1, i2, j1, j2)
    ret += i1*j1*cnt_b[N-1][N-1]
    if i2 > 0 and j2 > 0:
        ret += cnt_b[i2-1][j2-1]
    if j2 > 0:
        ret += cnt_b[N-1][j2-1]*i1
    if i2 > 0:
        ret += cnt_b[i2-1][N-1]*j1
    return ret

# クエリを処理
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = sum_b(C, D)
    # print('sum', sum_b(A-1, B-1), sum_b(C, D), sum_b(A-1, D), sum_b(C, B-1))
    if A-1 >= 0 and B-1 >=0:
        ans -= sum_b(A-1, D) + sum_b(C, B-1) - sum_b(A-1, B-1)
    elif A-1 >= 0:
        ans -= sum_b(A-1, D)
    elif B-1 >= 0:
        ans -= sum_b(C, B-1)
    print(ans)
