N, T = map(int, input().split())

p = {i+1: 0 for i in range(N)}
s = {0: N}
ans = 1
for _ in range(T):
    A, B = map(int, input().split())
    pp = p[A]
    p[A] += B
    ss = s.get(pp+B, 0)
    s[pp] -= 1
    s[pp+B] = ss + 1
    if s[pp] == 0:
        ans -= 1
    if s[pp+B] == 1:
        ans += 1
    print(ans)
