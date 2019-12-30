def run(N, M, A):
    A = sorted(A, reverse=True)
    right = A[0] * 2
    left = 0
    while left <= right:
        X = (left + right) // 2
        # 左手の相手がaで、満足度がX以上となる組合せの数
        cnt = 0
        for a in A:
            cnt += search(A, X - a)
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
