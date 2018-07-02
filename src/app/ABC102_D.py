from itertools import accumulate


def run(n, a):
    # sum_a = [sum(a[0:i+1]) for i in range(n)]
    sum_a = list(accumulate(a))
    li = 0
    ri = 2
    t = sum_a[-1]
    diff = sum_a[-1]
    # 真ん中の切れ込みを順に変更
    # 左の切れ込みの位置はiに対して単調増加
    # 左の切れ込みで真ん中の項を移動するかどうかは、
    # 真ん中の項を除いて、小さい方に入れる
    # ただし単調増加なので、左の切れ込みの左側が
    # 小さいときに真ん中を左の切れ込みの左側に入れる
    # 右も同様に考える
    for i in range(1, n-2):
        while sum_a[i] > sum_a[li+1] + sum_a[li]:
            li += 1
        while t + sum_a[i] > sum_a[ri+1] + sum_a[ri]:
            ri += 1
        p = sum_a[li]
        q = sum_a[i] - p
        r = sum_a[ri] - q - p
        s = t - sum_a[ri]
        diff = min(diff, max(p, q, r, s) - min(p, q, r, s))
    return diff


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
