import os
from solver import solve


files = os.listdir('sample')
for file in files:
    f = open('sample/' + file, 'r')
    data = f.read().split('\n')
    n, m = map(int, data[0].split())
    lattice = {}
    for x in range(n):
        for y in range(n):
            lattice[(x, y)] = -1
    x, y = [], []
    for i in range(m):
        xx, yy = map(int, data[i+1].split())
        x.append(xx)
        y.append(yy)
        lattice[(xx, yy)] = i

    k, ans = solve(n, m, x, y, lattice)
    print(k)
