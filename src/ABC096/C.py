def run(H, W, s):
    for y in range(H):
        for x in range(W):
            if check(s, H, W, y, x):
                continue
            else:
                return 'No'
    return 'Yes'


def check(s, H, W, y, x):
    '''
    sの(x, y)座標から見て、4方向をチェックする
    (x, y)が'#'の場合は、4方向のどこかに'#'があればTrue, なければFalse
    (x, y)が'.'の場合は、True
    '''
    ret = False
    if s[y][x] == '.':
        ret = True
    if x - 1 >= 0:
        if s[y][x-1] == '#':
            ret = True
    if x + 1 < W:
        if s[y][x+1] == '#':
            ret = True
    if y - 1 >= 0:
        if s[y-1][x] == '#':
            ret = True
    if y + 1 < H:
        if s[y+1][x] == '#':
            ret = True
    return ret


def main():
    H, W = map(int, input().split())
    s = []
    for i in range(H):
        s.append(input())
    print(run(H, W, s))


if __name__ == '__main__':
    main()
