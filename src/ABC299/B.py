N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

flg = False
cc = C[0]
max_t = -1
max_ti = 0
max_cc = -1
max_cci = 0
for i in range(N):
    c = C[i]
    r = R[i]
    if c == T:
        flg = True
        if max_t < r:
            max_t = r
            max_ti = i
    if c == cc:
        if max_cc < r:
            max_cc = r
            max_cci = i
if flg:
    print(max_ti+1)
else:
    print(max_cci+1)