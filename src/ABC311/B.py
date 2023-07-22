N, D = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
ans = 0
t_ans = 0
for i in range(D):
    flg = True
    for j in range(N):
        if S[j][i] == 'x':
            flg = False
            t_ans = 0
            break
    if flg:
        t_ans += 1
        ans = max(ans, t_ans)
print(ans)