N = int(input())

N -= 1
a = []
l = [0, 2, 4, 6, 8]
while N >= 5:
    a1 = N%5
    # print(N, a1)
    N -= a1
    N //= 5
    # print(N, a1)
    a.append(a1)
a.append(N)
# print(a)
ans = 0
for i in range(len(a)):
    a1 = a[i]
    ans += l[a1]*(10**i)

print(ans)
