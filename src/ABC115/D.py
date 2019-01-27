c = [1]
fnx = {(0, 0): 0, (0, 1): 1}


def run(N, X):
    '''
    Fn(X)をレベルNバーガーの下からX層のパティの数とする
    C(N)をレベルNバーガーの層の数とする
    C(N) = 3 + 2*C(N-1)
    X=1のとき、Fn(X) = 0
    1<X<=C(N-1)+1のとき、Fn(X) = Fn-1(X-1)
    X=C(N-1)+2のとき、Fn(X) = Fn-1(C(N-1)) + 1
    C(N-1)+2<X<=2*C(N-1)+2のとき、Fn(X) = Fn-1(C(N-1)) + Fn-1(X-C(N-1)-2) + 1
    X = 2*C(N-1)+3のとき、Fn(X) = 2*Fn-1(C(N-1)) + 1
    '''
    for i in range(N):
        c.append(3+2*c[i])
    return get_fnx(N, X)


def get_fnx(N, X):
    if (N, X) in fnx.keys():
        return fnx[(N, X)]
    if X <= 1:
        return 0
    elif X <= c[N-1] + 1:
        return get_fnx(N-1, X-1)
    elif X == c[N-1] + 2:
        return get_fnx(N-1, c[N-1]) + 1
    elif X <= 2*c[N-1] + 2:
        return get_fnx(N-1, c[N-1]) + get_fnx(N-1, X-c[N-1]-2) + 1
    else:
        return 2*get_fnx(N-1, c[N-1]) + 1


def main():
    N, X = map(int, input().split())
    print(run(N, X))


if __name__ == '__main__':
    main()
