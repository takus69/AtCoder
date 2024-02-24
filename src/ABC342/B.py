N = int(input())
P = list(map(int, input().split()))
P2 = {}
for i, p in enumerate(P):
    P2[p] = i
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    if P2[A] < P2[B]:
        print(A)
    else:
        print(B)
