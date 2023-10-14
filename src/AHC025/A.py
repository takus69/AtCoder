import random


random.seed(0)

# 初期設定
N, D, Q = map(int, input().split())
ans = [d for d in range(D)]
ans += [random.randint(0, D-1) for _ in range(D, N)]
print('#C', ' '.join(map(str, ans)))
q = 0  # クエリの回数

# 初期測定
def measure_d(dl, dr):
    nl = 0
    nr = 0
    l = []
    r = []
    for i in range(N):
        d = ans[i]
        if d == dl:
            nl += 1
            l.append(i)
        elif d == dr:
            nr += 1
            r.append(i)
    print(' '.join(map(str, [nl, nr] + l + r)))
    q = input()
    print('# {} {} {}'.format(dl, q, dr))
    return q
 
for d in range(D-1):
    q = measure_d(d, d+1)


D_cnt = {d: 0 for d in range(D)}
for d in ans:
    D_cnt[d] += 1

for i in range(Q):
   print('#C', ' '.join(map(str, ans)))
print(' '.join(map(str, ans)))
