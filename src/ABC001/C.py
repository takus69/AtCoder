def run(deg, dis):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
            'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    d_dir = 360 / len(dirs) * 10
    d_w = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7,
           24.4, 28.4, 32.6]
    dis = round2(dis / 60)
    dir = 'N'
    for i in range(len(dirs)):
        if deg < 112.5 + i * d_dir:
            dir = dirs[i]
            break
    w = 12
    for i in range(len(d_w)):
        if dis <= d_w[i]:
            w = i
            break
    if w == 0:
        dir = 'C'
    return '{} {}'.format(dir, w)


def round2(x):
    return ((10*x*2 + 1)//2)/10

def main():
    deg, dis = map(int, input().split())
    print(run(deg, dis))


if __name__ == '__main__':
    main()
