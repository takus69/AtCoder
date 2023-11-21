N, L = map(int, input().split())
A = []
for _ in range(L):
    A.append(input())
y = input()

for j in range(2*N-1):
    if y[j] == 'o':
        break
yj = j // 2

al, ar = ' ', ' '
for i in range(L):
    ni = L-1-i
    # print('before', N, L, ni, j)
    a = A[ni][j]
    if j-1 > 0:
        al = A[ni][j-1]
    if j+1 < 2*N-1:
        ar = A[ni][j+1]
    if al == '-':
        j -= 2
    elif ar == '-':
        j += 2
    al, ar = ' ', ' '
    # print('after', N, L, ni, j)
print(j//2 + 1)
