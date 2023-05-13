S = input()
N = int(input())

n_s = len(S)
ans = 0

for i in range(n_s):
    s = S[i]
    n2 = 2**(n_s-i-1)
    if s == '1':
        ans += n2
for i in range(n_s):
    s = S[i]
    n2 = 2**(n_s-i-1)
    if s == '?': 
        if ans + n2 <= N:
            ans += n2
if ans > N:
    ans = -1

print(ans)
