def run(A, B, C, X, Y):
    '''
    以下のうち一番安い金額を出力する
    - A, Bピザ両方単独で買う
    - ABピザで少ない方全部まで買い、残りは単独で買う
    - ABピザで全部買う
    '''
    max_XY = max(X, Y)
    min_XY = min(X, Y)
    diff = max_XY - min_XY
    if X > Y:
        D = A
    else:
        D = B
    ret = A*X + B*Y
    ret = min(ret, min_XY*C*2 + diff*D)
    ret = min(ret, max_XY*C*2)
    return ret


def main():
    A, B, C, X, Y = map(int, input().split())
    print(run(A, B, C, X, Y))


if __name__ == '__main__':
    main()
