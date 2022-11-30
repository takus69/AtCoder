T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    ret = 10**10
    for k in range(1, int(B**(1/2))+1):
        X = max(int(B/k - A)+1, int((B-k*A)/(k+1))+1)
        ret = min(k*A + (k+1)*X - B, ret)
    print(ret)