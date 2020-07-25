N = int(input())

# f(n)を事前に計算
f = {}

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            n = x**2 + y**2 + z**2 + x*y + y*z + z*x
            f[n] = f.get(n, 0) + 1

for i in range(1, N+1):
    print(f.get(i, 0))
