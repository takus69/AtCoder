A, M, L, R = map(int, input().split())

ans = (R-A)//M - (L-A)//M + 1
if (L-A) % M != 0:
    # print(L-A, M, '-')
    ans -= 1
print(ans)
