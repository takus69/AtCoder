import sys


N = int(input())
X_bin = input()

X_int = int(X_bin, 2)  # bin => int
dp = {1: 1}
bin_cnt = {}

sys.setrecursionlimit(10**5)


def calc_bin_cnt(next_int):
    if next_int in bin_cnt.keys():
        cnt = bin_cnt[next_int]
    else:
        next_bin = format(next_int, 'b')
        # popcount
        cnt = 0
        for i in next_bin:
            if i == '1':
                cnt += 1
    return cnt


def calc_ans(next_int):
    ans = 0
    while next_int > 0:
        key = next_int
        if key in dp.keys():
            ans += dp[key]
            break
        else:
            cnt = calc_bin_cnt(next_int)
            bin_cnt[next_int] = cnt
            next_int = next_int % cnt
            ans += 1
            dp[key] = ans
    return ans


for i in range(N):
    if X_bin[i] == '1':
        print(calc_ans(X_int - (2**(N-i-1))))
    else:
        print(calc_ans(X_int + (2**(N-i-1))))
