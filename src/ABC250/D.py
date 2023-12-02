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

ps = primes(int(N**(1/3)))
# print(len(ps))

ans = 0
for i in range(len(ps)):
    p = ps[i]
    if p**4 > N:
        break
    l, r = i+1, len(ps)-1
    if p*(ps[r]**3) <= N:
        ans += r-i
        continue
    elif p*(ps[l]**3) > N:
        continue
    else:
        while True:
            # print('l, r:', l, r)
            m = (l+r)//2
            if p*(ps[m]**3) <= N:
                l = m
            else:
                r = m
            if l+1 == r:
                ans += l-i
                break

print(ans)
