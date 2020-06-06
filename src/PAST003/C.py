A, R, N = map(int, input().split())

ans = A

if R >= 2 and N >= 31:
    ans = 'large'
elif R == 1:
    ans = A
else:
    for i in range(N):
        if i != 0:
            ans *= R
        if ans > 10**9:
            ans = 'large'
            break

print(ans)
