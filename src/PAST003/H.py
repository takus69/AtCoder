N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())


def add_time(x1, x2, x3, x4):
    '''
    4つずつ進むときの時間
    引数は障害物があるか
    '''
    t3 = T1 + T2*3  # 行動3
    t1111 = T1*4  # 行動1111
    if x1:
        t1111 += T3
    if x2:
        t1111 += T3
    if x3:
        t1111 += T3
    t22 = T1*2 + T2*2  # 行動22
    if x2:
        t22 += T3
    t112 = T1*3 + T2  # 行動112, 121, 211
    t121 = t112
    t211 = t112
    if x1:
        t112 += T3
        t121 += T3
    if x2:
        t112 += T3
        t211 += T3
    if x3:
        t121 += T3
        t211 += T3
    t = min(t3, t1111, t22, t112, t121, t211)
    if x0:
        t += T3
    return t


shou = L // 4
amari = L % 4
ans = 0
x_i = 0
now = 0
if now == x[x_i]:
    ans += T3
for i in range(shou):
    now = 4*i
    if now + 1 == x[x_i]:
        x1 = True
        x_i += 1
    else:
        x1 = False
    if now + 2 == x[x_i]:
        x2 = True
        x_i += 1
    else:
        x2 = False
    if now + 3 == x[x_i]:
        x3 = True
        x_i += 1
    else:
        x3 = False
    if now + 4 == x[x_i]:
        x4 = True
        x_i += 1
    ans += add_time(x1, x2, x3, x4)
    print(ans)

# 残りの部分
now = shou * 4
if amari == 1:
    t = min(T1, T1*(1/2) + T2*(1/2))
    if now == x[x_i]:
        t += T3
    ans += t

print(ans)
