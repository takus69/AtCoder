def gcd(x, y):
    '''ユークリッド互除法(math.gcd)'''
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

def modint(P, Q, MOD):
    '''有理数P/QのMODを算出'''
    return (P * pow(Q, -1, MOD)) % MOD

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

def prime_factorization(n):
    '''素因数分解'''
    primes = {}
    i = 2
    while i*i <= n:
        if n%i==0:
            n //= i
            primes[i] = primes.get(i, 0)+1
        else:
            i += 1
    if n > 1:
        primes[n] = primes.get(n, 0)+1
    return primes


if __name__ == '__main__':
    msg = 'test for gcd'
    assert gcd(5, 3) == 1, msg
    assert gcd(12, 4) == 4, msg

    msg = 'test for primes'
    assert primes(6) == [2, 3, 5], msg
    assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19], msg

    msg = 'test for prime factorization'
    assert prime_factorization(6) == {2:1, 3:1}
    assert prime_factorization(12) == {2:2, 3:1}
    assert prime_factorization(8) == {2:3}
