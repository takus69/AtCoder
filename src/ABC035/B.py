S = input()
T = int(input())

cnt = {'L': 0, 'R': 0, 'U': 0, 'D': 0, '?': 0}
for s in S:
    cnt[s] += 1

ans = abs(cnt['L'] - cnt['R']) + abs(cnt['U'] - cnt['D'])
if T == 1:
    ans += cnt['?']
else:
    ans -= cnt['?']
    if ans < 0:
        ans = abs(ans)
        ans %= 2

print(ans)
