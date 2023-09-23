N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

sum_A = [0]
temp_a = 0
for Ai in A:
    temp_a += Ai
    sum_A.append(temp_a)

sum_B = [0]
temp_b = 0
for Bi in B:
    temp_b += Bi
    sum_B.append(temp_b)

ans = 0
for Ai in A:
    l, r = -1, M - 1
    while True:
        m = (l + r) // 2 + 1
        if B[m] > P - Ai:
            r = m - 1
        else:
            l = m
        if l >= r:
            break
    # print(Ai, sum_B[l+1], P * (M-l-1), l, r, m)
    ans += (Ai * (l+1)) + sum_B[l+1] + (P * (M-l-1))

print(ans)
