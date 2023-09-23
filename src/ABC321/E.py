import math


T = int(input())
for _ in range(T):
    N, X, K = map(int, input().split())
    ans = 0
    if K == 0:
        ans = 1
    elif math.log2(N) >= K:
        up_x = X
        down_x = X
        down_flg = True
        down_cnt = 0
        for i in range(1, K+1):
            up_x *= 2
            if down_flg:
                down_x //= 2
                if down_x == 1:
                    down_flg = False
            else:
                down_x = down_x*2 + 1
                down_cnt += 1
            if up_x > N:
                up_x = 0
            if down_x > N:
                down_x = 0
        if up_x == 0:
            ans += 0
        elif up_x + 2**K - 1 > N:
            ans += N - up_x + 1
        else:
            ans += 2**K
        if down_x == 0:
            ans += 0
        elif down_flg:
            ans += 1
        else:
            if down_x > N:
                ans += 2**down_cnt - (down_x - N)
            else:
                ans += 2**max(down_cnt-1, 0)
        # print(up_x, down_x, down_cnt, down_flg)
    print(ans)

