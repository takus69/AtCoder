def primes(n):
    '''
    エラトステネスの篩にて、n以下の素数リストを作成
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]


N, P = map(int, input().split())
if N > 1:
    prime_list = primes(int(P**(1/N)+1))
    prime_cnt = {p: 0 for p in prime_list}
    # print(prime_list)
    # print(prime_cnt)
    for p in prime_list:
        while P % p == 0:
            P //= p
            # print(P)
            prime_cnt[p] += 1
    ans = 1
    for p in prime_list:
        cnt = prime_cnt[p]
        # print(p, cnt, cnt % N)
        if cnt >= N:
            ans *= p ** (cnt // N)
else:
    ans = P
print(ans)
