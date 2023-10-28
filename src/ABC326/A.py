X, Y = map(int, input().split())
ans = 'Yes'
if Y - X > 2:
    ans = 'No'
elif X - Y > 3:
    ans = 'No'
print(ans)