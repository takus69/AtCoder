N = int(input())
X_bin = input()

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
    if next_int == 0:
        return 0
    if cnt is None:
        cnt = calc_bin_cnt(next_int)
    next_int = next_int % cnt
    if next_int > 0:
        ans = calc_ans(next_int) + 1
    else:
        ans = 1
    return ans


X_cnt = calc_bin_cnt(X_int)
for i in range(N):
    if X_bin[i] == '1':
        print(calc_ans(X_int - (2**(N-i-1)), X_cnt-1))
    else:
        print(calc_ans(X_int + (2**(N-i-1)), X_cnt+1))
