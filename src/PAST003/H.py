N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

block_time = {i: 0 for i in range(L)}
x_i = 0
for i in range(L):
    if x_i >= N:
        break
    if x[x_i] == i:
        block_time[i] = T3
        x_i += 1


def add_run(i, dp, x_i, x):
    '''
    i: 今の位置
    dp: iの位置に着地する最小の時間
    x_i: 今まで通ってない障害物のインデックスの最小値
    x: 障害物の場所
    '''
    # 行動1
    a1 = dp[i-1] + T1 + block_time[i-1]
    # 行動2
    if i-2 < 0:
        a2 = 10**9
    else:
        a2 = dp[i-2] + T1 + T2 + block_time[i-2]
    # 行動3
    if i-4 < 0:
        a3 = 10**9
    else:
        a3 = dp[i-4] + T1 + 3*T2 + block_time[i-4]

    # ジャンプでゴールする場合
    if i == L:
        # 行動2
        a2_j = dp[i-1] + T1//2 + T2//2 + block_time[i-1]
        # 行動3
        a3_j1 = dp[i-1] + T1//2 + T2//2 + block_time[i-1]
        if i-2 >= 0:
            a3_j2 = dp[i-2] + T1//2 + T2 + T2//2 + block_time[i-2]
        else:
            a3_j2 = 10**9
        if i-3 >= 0:
            a3_j3 = dp[i-3] + T1//2 + 2*T2 + T2//2 + block_time[i-3]
        else:
            a3_j3 = 10**9
    else:
        a2_j = 10**9
        a3_j1 = 10**9
        a3_j2 = 10**9
        a3_j3 = 10**9

    dp[i] = min(a1, a2, a3, a2_j, a3_j1, a3_j2, a3_j3)


if __name__ == '__main__':
    dp = [0 for _ in range(L+1)]
    x_i = 1

    for i in range(1, L+1):
        # print(i, dp, x_i, x)
        add_run(i, dp, x_i, x)
print(dp[-1])
