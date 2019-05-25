def run(N, K, A):
    '''
    K <= 10^12 ~= 2^40
    Kの2進数における各桁ごとの最大となるKを求めることができる(O(logK))
    Kの2進数における最初の1を0に変える位置をk_nとする
    最初に変える位置の前はすべてKと同じ、それ以降は最大を取るものを選択する(O(log(K)))
    k_nが0の場合は、全て同じパターンとしてスキップする
    上記の最大のものを習得する
    '''
    cnt1 = []

    # Kの2進数の桁を取得
    k_n = len(bin(K)) - 2

    # Aの2進数の最大桁を取得
    max_a = len(bin(max(A))) - 2
    max_a = max(max_a, k_n)

    # 数値をビットに変換
    K_bit = '{:b}'.format(K).zfill(max_a)
    A_bit = []
    for i in range(len(A)):
        A_bit.append('{:b}'.format(A[i]).zfill(max_a))

    # 2進数の各桁の値を事前計算
    bit_v = []
    for i in range(max_a):
        bit_v.append(2**(max_a-i-1))

    # A_bitの各桁の1の数を数える(O(NlogK))
    for j in range(max_a):
        cnt = 0
        for i in range(N):
            if A_bit[i][j] == '1':
                cnt += 1
        cnt1.append(cnt)

    # Kの上からi+1桁目を1=>0にすると考える
    # k_n+1桁目の場合はすべて同じ場合
    ret = 1
    for i in range(k_n+1):
        tmp1 = 0
        max_flg = False
        for j in range(max_a):
            if max_a - j == k_n - i:  # Kの対象桁を0とするパターン
                # 1だと0に変える、0だと0のまま
                tmp1 += bit_v[j] * cnt1[j]
                # 1=>0の時はフラグを付与
                if K_bit[j] == '1':
                    max_flg = True
            elif not max_flg:  # Kの各桁をそのままに使うパターン
                # K[j]が0だとcnt1[j]を、1だとN-cnt1[j]をかける
                tmp1 += bit_v[j] * (cnt1[j]**(1-int(K_bit[j]))) * ((N-cnt1[j])**(int(K_bit[j])))
            else:  # Kの前の桁で1=>0として、その後は最大になるようにとるパターン
                tmp1 += bit_v[j] * max(cnt1[j], N - cnt1[j])
        ret = max(ret, tmp1)
    return ret


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(run(N, K, A))


if __name__ == '__main__':
    main()
