def run(s):
    n = 1000001
    a = [0, s]
    for i in range(2, n):
        pre = a[i-1]
        if pre % 2 == 0:
            a.append(pre // 2)
        else:
            a.append(3*pre + 1)
    ret_dic = {}
    ret = None
    for i in range(1, n):
        ai = a[i]
        if ai in ret_dic:
            ret = i
            break
        else:
            ret_dic[ai] = 1
    return ret


def main():
    s = int(input())
    print(run(s))


if __name__ == '__main__':
    main()
