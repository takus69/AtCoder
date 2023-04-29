H, W = map(int, input().split())
A = []
B = []
for _ in range(H):
    A.append(list(input()))
for _ in range(H):
    B.append(list(input()))

# print(H, W, len(A), len(A[0]), A, A[0])
ans = 'No'
for s in range(H):
    for t in range(W):
        # 一致確認
        flg = True
        for i in range(H):
            for j in range(W):
                if B[i][j] != A[(i+s)%H][(j+t)%W]:
                    flg = False
        if flg:
            ans = 'Yes'
            break
print(ans)
