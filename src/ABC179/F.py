N, Q = map(int, input().split())

ans = (N-2)**2
wall1 = [N-1]*N
wall2 = [N-1]*N
H, W = N, N
#wall1 = {N: N}  # key列までの白石の最小の行数
#wi1 = [N]  # wall1のkeyを格納。最小の値しか入ってこないため後ろに追加すれば、ソートされている
#wic1 = 1  # wi1の個数を保持
#wall2 = {N: N}
#wi2 = [N]
#wic2 = 1

'''
def search(x, wi, wic):
    wiからxより大きい最小の値を検索する
    l, r = 0, wic-1
    ret = 0
    while True:
        m = (l+r)//2
        if wi[m] >= x:
            l = m
            ret = m
        else:
            r = m
        if r-l == 1:
            l = r
        if l == r == m:
            break
    return ret
'''


for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        #i1 = search(x, wi1, wic1)  # 二分探索
        #uc = wall1[wi1[i1]]
        #ans -= uc - 2
        #i2 = search(uc, wi2, wic2)
        #print('1:', wall2[wi2[i2]], uc)
        #if wall2[wi2[i2]] > x:
        #    wi2.append(uc)
        #    wall2[uc] = x
        #    wic2 += 1
        if x < W:
            for i in range(x-1, W):
                wall1[i] = H-1
            W = x
        ans -= wall1[x-1] - 1
    else:
        if x < H:
            for i in range(x-1, H):
                wall2[i] = W-1
            H = x
        ans -= wall2[x-1] - 1
    #print(c, x, wall1, wall2, ans, W, H)
print(ans)
