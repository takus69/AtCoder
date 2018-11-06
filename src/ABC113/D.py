def run(H, W, K):
    # あみだくじの通る道のパターン
    dp = {(1, 0): 1}
    for w in range(2, W+1):
        dp[(w, 0)] = 0
    # ダミーで0とW+1には0を入れておく
    for h in range(0, H+1):
        dp[(0, h)] = 0
        dp[(W+1, h)] = 0
    # あみだくじの通る道のパターンを計算
    for h in range(1, H+1):
        for w in range(1, W+1):
            '''
            hの位置で他の線のパターンを計算
            w-1からwの線があるとき
            1からw-2までw-3本の線が引ける、w+1からWまでW-w-1本の線が引ける
            1本なら2パターン、2本なら3パターン、3本なら5パターン、4本なら1+4+3=8パターン
            5本なら1+5+6+1=13パターン、6本なら1+6+10+4=21、7本なら1+7+15+10+1=34パターン
            ''' 
            a = get_coef(w-3, W-w-1)
            b = get_coef(w-2, W-w-1)
            c = get_coef(w-2, W-w-2)
            dp[(w, h)] = (a*dp[(w-1, h-1)] + b*dp[(w, h-1)] + c*dp[(w+1, h-1)]) % 1000000007
    # あみだのKに行くための経路の合計
    return dp[K, H]


def get_coef(w_l, w_r):
    coef = [1, 2, 3, 5, 8, 13, 21, 34]
    if w_l < 0:
        w_l = 0
    if w_r < 0:
        w_r = 0
    return coef[w_l]*coef[w_r]


def main():
    H, W, K = map(int, input().split())
    print(run(H, W, K))


if __name__ == '__main__':
    main()
