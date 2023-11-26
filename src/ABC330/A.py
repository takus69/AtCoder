N, L = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    if a >= L:
        cnt += 1
print(cnt)
