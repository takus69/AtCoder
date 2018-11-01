def run(N):
    p_list = primes(555555)
    # 選択した素数が、5で割って余りが1のもののみ選択すれば、必ず合成数になる
    ret = []
    for p in p_list:
        if p % 5 == 1:
            ret.append(p)
        if len(ret) == N:
            break
    return ' '.join([str(p) for p in ret])


def primes(n):
    '''
    エラトステネスの篩にて、素数のリストを作成
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
