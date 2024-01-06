N, Q = map(int, input().split())
fp = [(N-i, 0) for i in range(N)]  # 足跡(footprint)
mv = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
for _ in range(Q):
    q1, q2 = input().split()
    if q1 == '1':
        x, y = fp[-1][0]+mv[q2][0], fp[-1][1]+mv[q2][1]
        fp.append((x, y))
    else:
        x, y = fp[-int(q2)]
        print(f'{x} {y}')
