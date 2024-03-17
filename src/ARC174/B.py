T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans = 0
    A1 = A[0]-A[4]
    A2 = A[1]-A[3]
    A2 += A1*2
    if A2 > 0:
        ans = min(P[3]*A2, P[4]*((A2+1)//2))
        if A2%2==1:
            ans = min(ans, P[3]+P[4]*(A2//2))
    print(ans)
