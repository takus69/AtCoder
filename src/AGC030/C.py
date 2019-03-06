def run(K):
    n_max = 500
    '''
    K <= 500の場合は、n = Kとして1行につき1色を塗ればよい
        111
        222
        333
    Kが4の倍数の場合は、n = K/2以下の塗り方ができる
        1234
        5678
        3412
        7856
    上記でn+i+1色をi色に塗り替えても条件を満たす
        1234
        5178
        3412
        7851
    K = 1000の時は、n = 500で満たし、塗り替え操作で501～999まで表現できる
    '''
    n = 0
    trouts = []
    if K <= n_max:
        n = K
        for i in range(K):
            trouts.append([i+1]*K)
    else:
        n = n_max
        change = n_max*2 - K
        c1 = [i for i in range(1, n_max+1)]
        c2 = [i for i in range(2, change+1)] + [i for i in range(n_max+1, n_max*2+1-change)] + [1]
        for i in range(n_max):
            shift = (i//2) * 2
            if i % 2 == 0:
                trouts.append(c1[shift:] + c1[:shift])
            else:
                trouts.append(c2[shift:] + c2[:shift])
    return (n, trouts)


def main():
    K = int(input())
    n, trouts = run(K)
    print(n)
    for i in range(len(trouts)):
        print(' '.join(map(str, trouts[i])))


if __name__ == '__main__':
    main()
