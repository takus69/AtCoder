N, T = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)
T %= sum_A
for i in range(len(A)):
    T -= A[i]
    if T < 0:
        print(i+1, T+A[i])
        break
