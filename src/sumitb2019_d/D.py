import re

N = int(input())
S = input()

ans = 0
for i in range(1000):
    s = f'{i:03}'
    si = 0
    for j in range(N):
        if S[j] == s[si]:
            si += 1 
            if si == 3:
                ans += 1
                break
print(ans)
