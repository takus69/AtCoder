R, C = map(int, input().split())
B = []
for _ in range(R):
    B.append(list(input()))

for i in range(R):
    for j in range(C):
        if B[i][j] != '.' and B[i][j] != '#':
            b = int(B[i][j])
            B[i][j] = '.'
            for ii in range(-b, b+1):
                max_j = min(b-ii, b+ii)
                for jj in range(-max_j, max_j+1):
                    iii = i+ii
                    jjj = j+jj
                    if min(iii, jjj) >= 0 and iii < R and jjj < C:
                        if B[iii][jjj] == '#':
                            B[iii][jjj] = '.'
for bb in B:
    print(''.join(bb))