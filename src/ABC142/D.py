import math

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

A, B = map(int, input().split())
gcd = math.gcd(A, B)
primes = prime_factorization(gcd)
# print(gcd, primes)
print(len(primes)+1)
