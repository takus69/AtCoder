def run(N, Q, STX, D):
    # i = f(D) 時間を指定するとどこまで行けるかの事前計算
    # 範囲でもよい？
    f = {i for i in range(10 ^ 9+1)}
    for i in range(N):
        s, t, x = STX[i]
        # OK
        #s - x # 未満
        #t - x # 以上


    # Qの出発時間で順に出力
    return (N, Q, STX, D)


def main():
    N, Q = map(int, input().split())
    STX = []
    for _ in range(N):
        STX.append(list(map(int, input().split())))
    D = []
    for _ in range(Q):
        D = list(map(int, input().split()))
    ret = run(N, Q, STX, D)
    for i in range(ret):
        print(ret[i])


if __name__ == '__main__':
    main()
