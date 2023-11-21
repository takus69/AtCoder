n = int(input())

A = [0, 0, 1, 1]
for i in range(4, n):
    A.append((A[-1] + A[-2] + A[-3])%10007)
print(A[n-1])