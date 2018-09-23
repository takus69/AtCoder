def run(s, t):
    key_s = tuple(s)
    key_t = tuple(t)
    dic_s = {}
    dic_t = {}
    for key in key_s:
        dic_s[key] = s.count(key)
    for key in key_t:
        dic_t[key] = t.count(key)
    dic_s2 = {}
    for (key, count) in dic_s.items():
        if dic_t.get(key, 0) == count:
            pass
        else:
            dic_s2[key] = count
    dic_t2 = {}
    for (key, count) in dic_t.items():
        if dic_s.get(key, 0) == count:
            pass
        else:
            dic_t2[key] = count
    counts_s = dic_s2.values()
    counts_s = sorted(counts_s)
    counts_t = dic_t2.values()
    counts_t = sorted(counts_t)
    check = 0
    ti = []
    si = []
    while(len(counts_s) == 0):
        max_s = counts_s[len(counts_s)-1]
        max_t = counts_t[len(counts_t)-1]
        if max_s > max_t:
            check = max_t
            ti.append(len(counts_t)-1)
            for i in range(len(counts_t)-2, -1, -1):
                if check + counts_t[i] > max_s:
                    continue
                elif check + counts_t[i] == max_s:
                    ti.append(i)
                    check += counts_t[i]
                    break
                else:
                    ti.append(i)
                    check += counts_t[i]
            if check != max_s:
                break
            else:
                counts_s.pop()
                for i in ti:
                    counts_t.pop(i)
        elif max_s < max_t:
            check = max_s
            si.append(len(counts_s)-1)
            for i in range(len(counts_s)-2, -1, -1):
                if check + counts_s[i] > max_t:
                    continue
                elif check + counts_s[i] == max_t:
                    si.append(i)
                    check += counts_s[i]
                    break
                else:
                    si.append(i)
                    check += counts_s[i]
            if check != max_t:
                break
            else:
                counts_t.pop()
                for i in si:
                    counts_s.pop(i)
        else:
            counts_s.pop()
            counts_t.pop()
    if len(counts_t) == 0 and len(counts_s) == 0:
        return 'Yes'
    else:
        return 'No'


def main():
    s = input()
    t = input()
    print(run(s, t))


if __name__ == '__main__':
    main()
