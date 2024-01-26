K, T = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = 0
for ai in a:
    ans = max(2*ai-sum_a-1, ans)
print(ans)
