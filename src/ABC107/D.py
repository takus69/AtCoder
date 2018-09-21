def run(n, a):
    a = sorted(a)
    m = n//2
    print(m)
    for i in range(m, n):
        # a2の合計がm+1以上の場合は、a[i]が中央値以上
        a2 = [1 if ai >= a[i] else 0 for ai in a]
        a_len = len(a2)
        a_sum = sum(a2)
        # 各区間(l, r)の合計がlen//2+1以上の場合は、a[i]が中央値以上
        # 上記を満たす通りが、m+1以上の場合は、a[i]がm(問題文の配列)の中央値以上
        cnt = (a_len-a_sum+1)*(a_sum-m+1)
        print(a[i], a_len, a_sum, cnt)
        if cnt >= (2**n-1)//2+1:
            ret = a[i]
        else:
            return ret


def read_line():
    n = int(input())
    a = list(map(int, input().split()))
    return (n, a)


def main():
    n, a = read_line()
    print(run(n, a))


if __name__ == '__main__':
    main()
