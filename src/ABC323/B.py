N = int(input())
r = {}
for i in range(N):
    win = 0
    for s in input():
        if s == 'o':
            win += 1
    r[i+1] = win

r = sorted(r.items(), key=lambda x:x[1], reverse=True)
r = [str(k) for k, v in r]
print(' '.join(r))
