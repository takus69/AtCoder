T = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(T):
    N, D, K = map(int, input().split())

    g = gcd(N, D)
    a = N // g
    b = D // g
    ans = ((K-1)*D) % N + (K-1)//a
    print(ans)
    
    '''
    m = D//N
    l = N//D

    if l > 0:
        if l >= K:
            ans = ((K-1)*D) % N
        else:
            l_cnt = (K-1) // l
            ans = ((K-1)*D) % N + l_cnt
    else:
        ans = ((K-1)*D) % N
    print(ans)
    '''
