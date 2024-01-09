n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ans1 = a[-1]
ans2 = -1
diff = abs(ans1/2 - ans2)
for i in range(n-1):
    if diff > abs(ans1/2 - a[i]):
        ans2 = a[i]
        diff = abs(ans1/2 - a[i])
print(f'{ans1} {ans2}')
