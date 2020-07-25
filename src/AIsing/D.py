N = int(input())
X_bin = input()
#N = 10**5
#X_bin = '1' * N

X_int = int(X_bin, 2)  # bin => int


def calc_bin_cnt(next_int):
    if next_int == 0:
        return 0
    next_bin = bin(next_int)[2:]
    # popcount
    cnt = 0
    for i in next_bin:
        if i == '1':
            cnt += 1
    return cnt


def calc_ans(next_int, cnt=None):
    if next_cnt == 0:
        return 0
    if next_int == 0:
        return 1
    if cnt is None:
        cnt = calc_bin_cnt(next_int)
    next_int = next_int % cnt
    if next_int > 0:
        ans = calc_ans(next_int) + 1
    else:
        ans = 1
    return ans


X_cnt = calc_bin_cnt(X_int)
f_p = X_int % (X_cnt+1)
if X_cnt-1 == 0:
    f_m = 0
else:
    f_m = X_int % (X_cnt-1)
for i in range(N):
    if X_bin[i] == '1':
        next_cnt = X_cnt - 1
        if next_cnt == 0:
            next_int = 0
        else:
            next_int = f_m - pow(2, (N-i-1), next_cnt)  # マイナスでも正しく求まる？
    else:
        next_cnt = X_cnt + 1
        next_int = f_p + pow(2, (N-i-1), next_cnt)
    print(calc_ans(next_int, next_cnt))
    #calc_ans(next_cnt, next_cnt)
