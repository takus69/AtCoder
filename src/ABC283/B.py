N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        k = q[1]
        x = q[2]
        A[k-1] = x
    elif q[0] == 2:
        k = q[1]
        print(A[k-1])
