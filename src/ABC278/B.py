H, M = map(int, input().split())
ans = False

for h in range(H, 24):
    for m in range(M, 60):
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        hh = int(h[0]+m[0])
        mm = int(h[1]+m[1])
        if hh < 24 and mm < 60:
            print('{} {}'.format(h, m))
            ans = True
            break
    M = 0
    if ans:
        break
if ans == False:
    print(0, 0)
