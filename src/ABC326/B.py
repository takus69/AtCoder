N = int(input())
ans = None
for n in range(N, 1000):
    tmp = str(n)
    t1, t2, t3 = map(int, tmp)
    if t1 * t2 == t3:
        ans = tmp
        break
print(ans)
