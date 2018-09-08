def run(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    return '{} {} {} {}'.format(x3, y3, x4, y4)


def read_line():
    x1, y1, x2, y2 = map(int, input().split())
    return (x1, y1, x2, y2)


def main():
    x1, y1, x2, y2 = read_line()
    ret = run(x1, y1, x2, y2)
    print(ret)


if __name__ == '__main__':
    main()
