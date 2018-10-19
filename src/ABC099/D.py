def run(N, C, D, c):
    '''
    マス番号に応じて3色に塗る必要がある
    (i+j)%3が0, 1, 2それぞれに対して、何色が何個あるか計算しておく
    ある色に塗るコストを計算する
    0, 1, 2それぞれのC色のコストのパターンができる
    上記コストに対してC色から3色を選択する全パターンのうち最小のコストを求める
    '''
    color0 = {}
    color1 = {}
    color2 = {}
    for k in range(C):
        color0[k] = 0
        color1[k] = 0
        color2[k] = 0
    for i in range(N):
        for j in range(N):
            color = c[i][j] - 1
            if (i+j+2) % 3 == 0:
                color0[color] += 1
            elif (i+j+2) % 3 == 1:
                color1[color] += 1
            elif (i+j+2) % 3 == 2:
                color2[color] += 1
    cost0 = {}
    cost1 = {}
    cost2 = {}
    for k in range(C):
        cost0[k] = 0
        cost1[k] = 0
        cost2[k] = 0
        for i in range(C):
            cost = D[i][k]
            cost0[k] += cost * color0[i] 
            cost1[k] += cost * color1[i] 
            cost2[k] += cost * color2[i] 
    ret = max(cost0.values()) + max(cost1.values()) + max(cost2.values())
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                else:
                    ret = min(ret, cost0[i]+cost1[j]+cost2[k])
    return ret


def main():
    N, C = map(int, input().split())
    D = []
    for i in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for i in range(N):
        c.append(list(map(int, input().split())))
    print(run(N, C, D, c))


if __name__ == '__main__':
    main()
