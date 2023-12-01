H, W = map(int, input().split())
A = ['.'*(W+2)]
for _ in range(H):
    A.append('.'+input()+'.')
A.append('.'*(W+2))
# print(A)
i, j = 1, 1
ans = 'Possible'
while True:
    # print('while', i, j)
    if A[i-1][j] == '#' and A[i][j-1] == '#':
        ans = 'Impossible'
        break
    elif A[i+1][j] == '#' and A[i][j+1] == '#':
        ans = 'Impossible'
        break
    if A[i+1][j] == '#':
        i += 1
    elif A[i][j+1] == '#':
        j += 1
    if i == H and j == W:
        if A[i-1][j] == '#' and A[i][j-1] == '#':
            ans = 'Impossible'
        elif A[i+1][j] == '#' and A[i][j+1] == '#':
            ans = 'Impossible'
        break

print(ans)
