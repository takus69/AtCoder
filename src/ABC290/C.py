N, K = map(int, input().split())
A = list(map(int, input().split()))
check = [0]*K

for a in A:
    if a < K:
        check[a] = 1

ans = 0
for i in range(len(check)):
    if check[i] == 1:
        ans += 1
    else:
        break
print(ans)