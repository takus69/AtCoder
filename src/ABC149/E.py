def run(N, M, A):
    '''
    Aiが10^5なので、searchを以下に変えられる
    サイズ10**5のリストで、その満足度を持つ数の件数を事前計算しておけばO(1)で求められる
    '''
    A = sorted(A, reverse=True)
    cnt_A = [len(A)]
    pre_a = 0
    cnt_dict_A = {}
    for a in sorted(A):
        cnt_dict_A[a] = cnt_dict_A.get(a, 0) + 1
    next_cnt = cnt_A[-1]
    for a in sorted(cnt_dict_A.keys()):
        cnt_A.extend([next_cnt]*(a-pre_a))
        pre_a = a
        next_cnt = cnt_A[-1]-cnt_dict_A[a]
    right = A[0] * 2
    left = 0
    while left <= right:
        X = (left + right) // 2
        # 左手の相手がaで、満足度がX以上となる組合せの数
        cnt = 0
        for a in A:
            # cnt += search(A, X - a)
            if X - a <= A[0]:
                if X - a >= 0:
                    cnt += cnt_A[X - a]
                else:
                    cnt += cnt_A[0]
        if cnt >= M:
            res = X
            left = X + 1
        else:
            right = X - 1
    X = res
    # Xが決まったので、累積和で組合せの数分の値を求める
    sum_A = [0]
    for a in sorted(A):
        sum_A.append(sum_A[-1] + a)
    sum_cnt = 0
    ans = 0
    for a in A:
        cnt = search(A, X - a)
        sum_cnt += cnt
        if cnt > 0:
            ans += cnt * a + sum_A[-1] - sum_A[-cnt-1]
    if sum_cnt > M:
        ans -= X * (sum_cnt - M)
    return ans


def search(A, X):
    '''
    AのリストからX以上となる数値がいくつか探す
    Aはソート済み(降順)
    二分探索で実装O(logN)
    leftとrightはチェック未
    middleはループ終了後チェック済み
    '''
    left = 0
    right = len(A) - 1
    res = 0
    while left <= right:
        middle = (left + right) // 2
        if A[middle] >= X:
            res = middle + 1
            left = middle + 1
        else:
            right = middle - 1
    return res


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(run(N, M, A))


if __name__ == '__main__':
    main()
