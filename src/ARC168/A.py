N = int(input())
S = input()

ans = 0
cnt = 0
for s in S:
    if s == '>':
        cnt += 1
        ans += cnt
    else:
        cnt = 0
print(ans)
