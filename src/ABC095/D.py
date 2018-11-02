def run(N, C, XV):
    print(N, C, XV)
    # 右回り、左回りで食べる
    energy1 = 0
    tmp = 0
    for i in range(N):
        tmp += XV[i][1]
        if energy1 < tmp-XV[i][0]:
            energy1 = tmp-XV[i][0]
            max_x1 = XV[i][0]
            print(energy1, max_x1)
    energy2 = 0
    tmp = 0
    for i in range(N):
        tmp += XV[N-i-1][1]
        if energy2 < tmp-(C-XV[N-i-1][0]):
            energy2 = tmp-(C-XV[N-i-1][0])
            max_x2 = C-XV[N-i-1][0]
            print(energy2, max_x2)

    # 右回りで食べた後、左回りで食べる(右回りは距離2倍になる)
    energy3 = 0
    tmp = 0
    for i in range(N):
        tmp += XV[i][1]
        if energy3 < tmp-XV[i][0]*2:
            energy3 = tmp-XV[i][0]*2
            max_x3 = XV[i][0]
            print(energy3, max_x3)

    # 左回りで食べた後、右回りで食べる(左回りは距離2倍になる)
    energy4 = 0
    tmp = 0
    for i in range(N):
        tmp += XV[N-i-1][1]
        if energy4 < tmp-(C-XV[N-i-1][0])*2:
            energy4 = tmp-(C-XV[N-i-1][0])*2
            max_x4 = C-XV[N-i-1][0]
            print(energy4, max_x4)
    print('energy')
    print(energy1, max_x1)
    print(energy2, max_x2)
    print(energy3, max_x3)
    print(energy4, max_x4)

    if C >= max_x2 + max_x3:
        energy3 = energy3 + energy2
    else:
        energy3 = 0
    if C >= max_x1 + max_x4:
        energy4 = energy1 + energy4
    else:
        energy4 = 0
    return max(energy1, energy2, energy3, energy4)


def main():
    N, C = map(int, input().split())
    XV = []
    for i in range(N):
        XV.append(list(map(int, input().split())))
    print(run(N, C, XV))


if __name__ == '__main__':
    main()
