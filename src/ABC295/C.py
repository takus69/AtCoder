N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

a1 = A[0]
ans = 0
i = 1
while i < N:
    a2 = A[i]
    if a1 == a2:
        ans += 1
        if i+1 < N:
            i += 1
            a1 = A[i]
    else:
        a1 = a2
    i += 1

print(ans)
