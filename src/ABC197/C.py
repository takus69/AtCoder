N = int(input())
A = list(map(int, input().split()))

ans = None
for i in range(2**(N-1)):
    b = bin(i)[2:]
    while len(b) < N-1:
        b = '0' + b

    tmp = A[0]
    xor = []
    for j in range(N-1):
        if b[j] == '1':
            xor.append(tmp)
            tmp = A[j+1]
        else:
            tmp |= A[j+1]
    xor.append(tmp)
    tmp = xor[0]
    for x in xor[1:]:
        tmp ^= x
    if ans is None:
        ans = tmp
    else:
        ans = min(tmp, ans)
print(ans)
