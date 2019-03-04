def run(K):
    '''
    K <= 500の場合は、n = Kとして1行につき1色を塗ればよい
        111
        222
        333
    Kが4の倍数の場合は、n = K/2として1行につき2色を交互に塗ればよい
        1212
        3434
        5656
        7878
    上記でi色をn+i色に塗り替えても条件を満たす
        1212
        3434
        1616
        7878
    K = 1000の時は、n = 500で満たし、塗り替え操作で501～999まで表現できる
    '''
    n = 0
    trouts = []
    if K <= 500:
        for i in range(K):
            n = K
            trouts.append([i+1]*K)
    else:
        change = 1000 - K
        c = [i for i in range(1, 501)] + [i for i in range(1, change+1)] + [i for i in range(501+change, 1001)]
        for i in range(500):
            trouts.append([c[2*i], c[2*i+1]]*250)
    return (n, trouts)


def main():
    K = int(input())
    n, trouts = run(K)
    print(n)
    for i in range(len(trouts)):
        print(' '.join(map(str, trouts[i])))


if __name__ == '__main__':
    main()
