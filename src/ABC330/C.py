D = int(input())

x = int(D**(1/2)) + 1
y = 0

ans = D
while True:
    # print(x, y)
    ans = min(ans, abs(x**2 + y**2 - D))
    if x**2 + y**2 > D:
        x -= 1
    else:
        y += 1
    if x < 0 or y > D**(1/2):
        break

print(ans)
