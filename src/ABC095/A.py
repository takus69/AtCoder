def run(s):
    ret = 700
    for si in s:
        if si == 'o':
            ret += 100
    return ret


def main():
    s = input()
    print(run(s))


if __name__ == '__main__':
    main()
