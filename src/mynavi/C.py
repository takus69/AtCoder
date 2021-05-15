def run(S):
    '''
    oは確実に入る
    ?は入るか分からない
    xは入らない
    oが4つ: 4!=24
    oが3つ: oのみでなる場合: 3x4C2x2x1=36, ?が入る場合: 4x?の数x3x2x1=?の数x24
    oが2つ: oのみでなる場合: 2-2: 4C2=6, 3-1: 4C1x2x1=8,
            ?が1つ入る場合: 4C1x?の数x3C2x2x1=?の数x24,
            ?が2つ1種類入る場合: 4C2x?の数x2x1=?の数x12, ?が2つ2種類入る場合: 4C2x?の数x(?の数-1)x2x1=?の数x(?の数-1)x12
    oが1つ: oのみの場合: 1
            ?が1つ入る場合: 4C1x1x?の数=?の数x4
            ?が2つ1種類入る場合: 4C2x?の数x1=?の数x6, ?が2つ2種類入る場合: 4C2x?の数x(?の数-1)x1=?の数x(?の数-1)x6
            ?が3つ1種類入る場合: 4C1x?の数=?の数x4, ?が3つ2種類入る場合: 4C2x?の数x2x(?の数-1)x1=?の数x(?の数-1)x12, ?が3つ3種類入る場合: 4C1x1x?の数x(?の数-1)x(?の数-2)
    oが0つ: ?が1種類入る場合: ?の数
            ?が2種類入る場合: 3-1: 4C1x?の数x(?の数-1), 2-2: 4C2x?の数x(?の数-1)/2
            ?が3種類入る場合: 2-1-1: 4C2x?の数x(?の数-1)x(?の数-2)
            ?が4種類入る場合: (?の数)!
    '''
    n_o = 0
    n_x = 0
    n_q = 0
    for s in S:
        if s == 'o':
            n_o += 1
        elif s == 'x':
            n_x += 1
        else:
            n_q += 1
    if n_o > 4:
        ans = 0
    elif n_o == 4:
        ans = 24
    elif n_o == 3:
        ans = 36 + n_q*24
    elif n_o == 2:
        ans = 6 + 8 + n_q*24 + n_q*12 + n_q*(n_q-1)*12
    elif n_o == 1:
        ans = 1 + n_q*4 + n_q*6 + n_q*(n_q-1)*6 + n_q*4 + n_q*(n_q-1)*12 + 4*n_q*(n_q-1)*(n_q-2)
    else:
        ans = n_q + 4*n_q*(n_q-1) + 3*n_q*(n_q-1) + 6*n_q*(n_q-1)*(n_q-2) + n_q*(n_q-1)*(n_q-2)*(n_q-3)
    # 全探索
    '''
    ans = 0
    for i in range(10000):
        s_i = str(i).zfill(4)
        flg = True
        for j in range(10):
            if S[j] == 'o':
                if str(j) in s_i:
                    None
                else:
                    flg = False
            if S[j] == 'x':
                if str(j) in s_i:
                    flg = False
        if flg:
            ans += 1
    '''
    return ans
 
def main():
    S = input()
    print(run(S))
 
if __name__ == '__main__':
    main()
