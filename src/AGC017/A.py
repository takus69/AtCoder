import math

N, P = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] %= 2
n_odd = sum(A)
n_even = N-n_odd
ans = 2**n_even
# print('n_odd, n_even', n_odd, n_even)
# print('ans', ans)
tmp = 0
for i in range(P, n_odd+1, 2):
    # print('i, n_odd', i, n_odd)
    tmp += math.factorial(n_odd) // (math.factorial(i) * math.factorial(n_odd-i))
    # print('i, tmp', i, tmp)
ans *= tmp
if P == 1 and n_odd == 0:
    ans = 0

print(ans)
