# import collections


def run(s, t):
    sc = {}
    tc = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        sc[i] = 0
        tc[i] = 0
    counter = 1
    for ss in s:
        if sc[ss] == 0:
            sc[ss] = counter
            counter += 1
    counter = 1
    for tt in t:
        if tc[tt] == 0:
            tc[tt] = counter
            counter += 1
    slist = [sc[ss] for ss in s]
    tlist = [tc[tt] for tt in t]
    if slist == tlist:
        return 'Yes'
    else:
        return 'No'
    '''
    ss = sorted(list(collections.Counter(s).values()))
    tt = sorted(list(collections.Counter(t).values()))
    if ss == tt:
        return 'Yes'
    else:
        return 'No'
    '''


def main():
    s = input()
    t = input()
    print(run(s, t))


if __name__ == '__main__':
    main()
