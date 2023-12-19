N = int(input())
a = list(map(int, input().split()))

base = 0
for ai in a:
    base ^= ai
ans = []
for ai in a:
    ans.append(ai^base)

print(' '.join(map(str, ans)))
