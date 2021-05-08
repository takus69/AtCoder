T = int(input())
cases = []
for _ in range(T):
    N = int(input())
    K = []
    L = []
    R = []
    D = []
    k, l, r = map(int, input().split())
    K.append(k)
    L.append(l)
    R.append(r)
    D.append(l-r)

    # 差分の降順にソート
    idx = [*range(len(N))]
    s_i = sorted(idx, key=lambda i: -D[i])

    num = {}  # K番目以上の数
    ans = 0
    for i in s_i:
        D_i = D[i]
        k_i = K[i]
        K_num = num.get(k_i, 0)
        if D_i > 0:
            if K_num < k_i:
                num[k_i] = K_num + 1
                ans += L[i]
            else:
                num
        elif D_i < 0:

        else:
            ans += L[i]  # どっちを足してもいい。どこでもいい
