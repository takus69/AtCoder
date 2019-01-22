def run(L, N, X):
    '''
    最初に向きを変える点をsとする
    その後は向きを変えながら最後の点まで行けばよい
    最後の点をfとする
    ある点をiと置く
    0からiの左回りの距離をli, 右回りの距離をriと置くと
    全体の距離は2*liのsからfの和と2*riのNからfの和を加算し
    最後の回りが左回りなら上記からlf+2*rfを減算し、
    右回りなら2*lf+rfを減算すれば全体の距離がでる
    sを1からfの場合すべてを求め、その最大値を出力すればよい
    ただし最初の回る方向が右と左両方を求める必要がある
    累積和を使えば、2*liのsからfの和をO(1)で求められる
    '''
    # 累積和取得
    l_sum = {0: 0}
    r_sum = {N+1: 0}
    for i in range(1, N+1):
        l_sum[i] = l_sum[i-1] + X[i-1]
    for i in range(N, 0, -1):
        r_sum[i] = r_sum[i+1] + L - X[i-1]
    # 開始左回り
    ret = 0
    for s in range(1, N+1):
        # 折り返す点の数
        nodes = (N - s + 1)
        # 最終地点
        f = int(s + (nodes - (nodes % 2)) / 2)
        if nodes % 2 == 1:
            last_dir_l = True
        else:
            last_dir_l = False
        if last_dir_l:
            tmp = 2*(l_sum[f] - l_sum[s-1]) + 2*(r_sum[f+1]) - X[f-1]
        else:
            tmp = 2*(l_sum[f-1] - l_sum[s-1]) + 2*(r_sum[f]) - (L - X[f-1])
        ret = max(ret, tmp)

    # 開始右回り
    for s in range(1, N+1):
        # 折り返す点の数
        nodes = s
        # 最終地点
        f = int((nodes + (nodes % 2)) / 2)
        if nodes % 2 == 1:
            last_dir_r = True
        else:
            last_dir_r = False
        if last_dir_r:
            tmp = 2*(l_sum[f-1]) + 2*(r_sum[f] - r_sum[s+1]) - (L - X[f-1])
        else:
            tmp = 2*(l_sum[f]) + 2*(r_sum[f+1] - r_sum[s+1]) - X[f-1]
        ret = max(ret, tmp)
    return ret


def main():
    L, N = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(int(input()))
    print(run(L, N, X))


if __name__ == '__main__':
    main()
