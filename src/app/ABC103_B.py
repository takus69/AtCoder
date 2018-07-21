def run(s, t):
    len_t = len(t)
    for i in range(len_t):
        t = t[-1] + t[0:(len_t-1)]
        if s == t:
            return 'Yes'
    return 'No'


def read_line():
    s = input()
    t = input()
    return (s, t)


def main():
    s, t = read_line()
    ret = run(s, t)
    print(ret)


if __name__ == '__main__':
    main()
