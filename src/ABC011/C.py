N = int(input())
NG = []
for _ in range(3):
    NG.append(int(input()))

ans = 'YES'
now = N
cnt = 0
if N in NG:
    ans = 'NO'
else:
    while True:
        cnt += 1
        if cnt > 100:
            ans = 'NO'
            break
        if now-3 in NG:
            if now-2 in NG:
                if now-1 in NG:
                    ans = 'NO'
                    break
                else:
                    now -= 1
            else:
                now -= 2
        else:
            now -= 3
        if now <= 0:
            break

print(ans)
