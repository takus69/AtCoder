N, K = map(int, input().split())
S = input()

cnt = 0
ans = ''
for i in range(N):
    if S[i] == 'o' and cnt < K:
        cnt += 1
        ans += 'o'
    else:
        ans += 'x'

print(ans)
