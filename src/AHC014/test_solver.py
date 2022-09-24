import os
from solver import solve


files = os.listdir('sample')
scores = []
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

    c = (n - 1) / 2
    s = 0
    for i in range(n):
        for j in range(n):
            s += (i-c)**2 + (j-c)**2 + 1
    q = 0
    for i, j in lattice.keys():
        if lattice[(i, j)] >= 0:
            q += (i-c)**2 + (j-c)**2 + 1
    score = round(10**6 * n * n / m * q / s)
    scores.append(score)

    print(file, k, score)
average_score = sum(scores) / len(scores)
print('average score:', average_score, 'expected score:', average_score*50)
