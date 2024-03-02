N = int(input())

target = []
for x in range(1, 10**6+1):
    K = x**3
    K = str(K)
    l = len(K) // 2
    if l == 0:
        target.append(int(K))
    elif K[:l] == K[-l:][len(K)::-1]:
        target.append(int(K))

ans = 1
for K in target:
    if K > N:
        break
    else:
        ans = K
print(ans)
