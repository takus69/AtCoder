X, Y, Z = map(int, input().split())
S = input()

A = []
C = []

now = S[0]
cnt = 0
cnt_A = 0
cnt_a = 0
for s in S:
    if now != s:
        A.append(now)
        C.append(cnt)
        if now == 'A':
            cnt_A += cnt
        else:
            cnt_a += cnt
        now = s
        cnt = 1
    else:
        cnt += 1
A.append(now)
C.append(cnt)
if now == 'A':
    cnt_A += cnt
else:
    cnt_a += cnt

caps = False
ans = 0
for i in range(len(A)):
    now = A[i]
    cnt = C[i]
    if now == 'A':
        cnt_A -= cnt
    else:
        cnt_a -= cnt
    print(caps, now, cnt, ans, cnt_A, cnt_a)
    if (caps and now == 'A') or (not caps and now == 'a'):
        if X*cnt == (Y*cnt + Z):
            ans += X*cnt
            if (cnt_A < cnt_a and X < Y) or (cnt_A > cnt_a and X > Y):
                caps = not caps
        elif X*cnt > (Y*cnt + Z):
            caps = not caps
            ans += Y*cnt + Z
        else:
            ans += X*cnt
    else:
        if (X*cnt + Z) == Y*cnt:
            ans += Y*cnt
            if (cnt_A < cnt_a and X > Y) or (cnt_A > cnt_a and X < Y):
                caps = not caps
        elif (X*cnt + Z) > Y*cnt:
            ans += Y*cnt
        else:
            caps = not caps
            ans += X*cnt + Z

print(ans)
