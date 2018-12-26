def run(N):
    # 3, 5, 7のみの数値を全列挙
    targets = make357(N)
    cnt = 0
    for t in targets:
        if all(t.count(s) for s in '357'):
            cnt += 1
    return cnt


def make357(N):
    '''
    3, 5 ,7のみを含むN以下の数を全列挙
    ただし文字列として格納
    '''
    targets = []
    targets_i = ['3', '5', '7']  # i桁の357のみを含む数
    for _ in range(1, len(str(N))):
        tmp = []
        for s in '357':
            tmp += [t + s for t in targets_i if int(t + s) <= N]
        targets_i = tmp
        targets += targets_i
    return targets


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
