N = int(input())
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
primes = primes(int(((N+1)/12)**(1/2))+1)
# print(len(primes))

ans = 0
a = 0
c = len(primes)-1
for c in range(len(primes)-1, 1, -1):
    for a in range(c-1):
        pa = primes[a]
        pc = primes[c]
        pb = primes[a+1]
        if pa**2 * pb * pc**2 > N:
            break
        i = a+1
        j = c-1
        while True:
            b = (i+j)//2
            pb = primes[b]
            if pa**2 * pb * pc**2 <= N:
                i = b
            else:
                j = b
            if i == j:
                ans += b-a
                break
            if i+1 == j:
                if pa**2 * primes[j] * pc**2 <= N:
                    i = j
                else:
                    j = i

print(ans)
