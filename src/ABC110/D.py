import math
import sys
import collections


mod = 1000000007
sys.setrecursionlimit(mod)
fact = {1: 1}


def run(n, m):
    # print('{}を{}個の数列で表現'.format(m, n))
    ans = 1
    primes = []
    for i in range(2, m):
        if m == 1:
            break
        if i*i > m:
            break
        if m % i == 0:
            cnt = 0
            while m % i == 0:
                cnt += 1
                m //= i
                primes.append(i)
            ans *= comb(cnt+n-1, n-1)
            ans %= mod
    # counts = collections.Counter(primes)
    # print(counts)
    # for (_, v) in counts.items():
    #     ans *= comb(v+n-1, n-1)
    #     ans %= mod
    if m != 1:
        ans *= n
        ans %= mod
    return ans


def comb(n, r):
    if r > (n-r):
        r = n-r
    mul = 1
    div = 1
    for i in range(r):
        mul *= n-i
        div *= i+1
        mul %= mod
        div %= mod
    # mul = math.factorial(n) // math.factorial(n - r)
    # div = math.factorial(r)
    # mul = factorial(n) // factorial(n - r)
    # div = factorial(r)
    mul %= mod
    div %= mod
    return (mul * modpow(div, (mod-2))) % mod


'''
def factorial(n):
    if n in fact:
        return fact[n]
    else:
        fact[n] = n*factorial(n-1)
        return fact[n]
'''


def modpow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        halfp = p // 2
        half = modpow(a, halfp)
        return int((half * half) % mod)
    else:
        return int((a * modpow(a, p-1)) % mod)


def main():
    n, m = map(int, input().split())
    print(run(n, m))


if __name__ == '__main__':
    main()
