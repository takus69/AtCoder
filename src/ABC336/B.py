N = int(input())
s = bin(N)
ans = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == '0':
        ans += 1
    else:
        break
print(ans)
