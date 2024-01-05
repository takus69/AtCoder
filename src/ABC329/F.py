N, Q = map(int, input().split())
C = list(map(int, input().split()))
C_cnt = {}
for c in C:
    C_cnt[c] = C_cnt.get(c, 0)+1
box = {}  # 各箱の[cnt, l]を保持。cntは1つの箱にしか入っていない色の種類の数。lは他の箱にも同じ色が入っているものの色のリスト
for i in range(1, N+1):
    cnt, l = 0, []
    c = C[i-1]
    if C_cnt[c] > 1:
        l = [c]
    else:
        cnt = 1
    box[i] = [cnt, l]

for _ in range(Q):
    a, b = map(int, input().split())
    a_cnt, a_l = box[a]
    b_cnt, b_l = box[b]
    # cnt
    b_cnt += a_cnt
    a_cnt = 0
    # l
    for c in a_l:
        flg = False
        for i in range(len(b_l)):
            if b_l[i] == c:
                flg = True
                break
        if flg:
            C_cnt[c] -= 1
            if C_cnt[c] == 1:
                b_cnt += 1
                del b_l[i]
        else:
            b_l.append(c)
    box[a] = [0, []]
    box[b] = [b_cnt, b_l]
    print(b_cnt+len(b_l))
