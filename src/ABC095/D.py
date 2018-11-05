def run(N, C, XV):
    '''
    左回りでxまで食べた後に、右回りのyまで食べると考える
    yは、xの次の皿まで食べることが可能なので、事前に最大
    となる食べ方を計算しておく
    逆回りも同様に計算して最大のものをとる
    '''
    # ある位置まで食べた時のカロリー
    cal_l = [0]
    cal_r = [0]
    # ある位置までの中で最大のカロリーとなるカロリー
    cal_max_l = [0]
    cal_max_r = [0]
    cal = 0
    for i in range(N):
        cal += XV[i][1]
        cal_l.append(cal-XV[i][0]*2)
        cal_max = cal_max_l[i]
        if cal_max < cal-XV[i][0]:
            cal_max = cal-XV[i][0]
        cal_max_l.append(cal_max)
    cal = 0
    for i in range(N):
        cal += XV[N-i-1][1]
        cal_r.append(cal-(C-XV[N-i-1][0])*2)
        cal_max = cal_max_r[i]
        if cal_max < cal-C+XV[N-i-1][0]:
            cal_max = cal-C+XV[N-i-1][0]
        cal_max_r.append(cal_max)

    ret = 0
    # 左回りが先
    for i in range(len(cal_l)):
        ret = max(ret, cal_l[i]+cal_max_r[N-i])
    # 右回りが先
    for i in range(len(cal_r)):
        ret = max(ret, cal_r[i]+cal_max_l[N-i])
    return ret


def main():
    N, C = map(int, input().split())
    XV = []
    for i in range(N):
        XV.append(list(map(int, input().split())))
    print(run(N, C, XV))


if __name__ == '__main__':
    main()
