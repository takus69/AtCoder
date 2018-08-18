def run(s, k):
    cnt = 0
    for si in s:
        si = int(si)
        if si == 1:
            cnt += 1
        else:
            return si
        if k == cnt:
            return 1


def read_line():
    s = input()
    k = int(input())
    return (s, k)


def main():
    s, k = read_line()
    print(run(s, k))


if __name__ == '__main__':
    main()
