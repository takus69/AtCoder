H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(list(map(int, input().split())))

sum_C = [[(0, 0) for _ in range(W+1)] for _ in range(H+1)]  # 各マスまでの濃度の累積和を保持する[b, w]
for i in range(1, H+1):
    for j in range(1, W+1):
        b, w = sum_C[i-1][j]
        b2, w2 = sum_C[i][j-1]
        b3, w3 = sum_C[i-1][j-1]
        b += b2 - b3
        w += w2 - w3
        if (i+j)%2 == 0:
            b += C[i-1][j-1]
        else:
            w += C[i-1][j-1]
        sum_C[i][j] = (b, w)

ans = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        B1, W1 = sum_C[i][j]
        for i2 in range(i):
            for j2 in range(j):
                B2, W2 = sum_C[i2][j2]
                B3, W3 = sum_C[i2][j]
                B4, W4 = sum_C[i][j2]
                if B1-B3-B4+B2 == W1-W3-W4+W2:
                    ans = max(ans, (i-i2)*(j-j2))
                    # print('(i, j)-(i2, j2)', (i, j), (i2, j2), B1-B3-B4+B2, W1-W3-W4+W2)
# for c in sum_C:
#     print(c)
print(ans)
