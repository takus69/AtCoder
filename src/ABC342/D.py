from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 素数のリスト取得
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

ps = primes(int(max(A)**(1/2))+1)

for i in range(N):
    a = A[i]
    if a == 0 or a == 1:
        continue
    for p in ps:
        p2 = p**2
        while a%p2 == 0:
            a //= p2
        A[i] = a

c = Counter(A)
ans = 0
for k, v in c.items():
    if k == 0:
        for i in range(v):
            ans += N-1-i
    else:
        ans += v*(v-1)//2
print(ans)
