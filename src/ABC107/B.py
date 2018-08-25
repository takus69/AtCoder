def run(h, w, a):
    ret1 = []
    for i in range(h):
        if a[i] != '.'*w:
            ret1.append(a[i])
    wi = []
    for i in range(len(ret1[0])):
        for j in range(len(ret1)):
            if ret1[j][i] == '#':
                wi.append(i)
                break
    ret = []
    for i in range(len(ret1)):
        s = ''
        for j in wi:
            s += ret1[i][j]
        ret.append(s)
    return ret


def read_line():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    return (h, w, a)


def main():
    h, w, a = read_line()
    ret = run(h, w, a)
    for i in range(len(ret)):
        print(ret[i])


if __name__ == '__main__':
    main()
