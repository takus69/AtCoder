def run(N):
    ret = []
    if N == 1:
        ret.append('Yes')
        ret.append(2)
        ret.append([[1, 1], [1, 1]])
    elif N < 3:
        ret.append('No')
    else:
        for i in range(3, N+1):
            if N * 2 < i * (i-1):
                ret.append('No')
                break
            elif N * 2 == i * (i-1):
                ret.append('Yes')
                ret.append(i)
                S = []
                for j in range(1, i+1):
                    '''
                    j列の1行目は、1列目のj行目
                    j列の2行目は、2列目のj行目
                    j列のk行目は、k列目のj行目
                    j列のj行目以降は、j-1列目の最後の行の数+1から1ずつ増加
                    '''
                    tmp = [i-1]
                    for k in range(1, i):
                        if k < j:
                            tmp.append(S[k-1][j-1])
                        else:
                            if j < 2:
                                tmp.append(k-j+1)
                            else:
                                tmp.append(S[j-2][i-1]+k-j+1)
                    S.append(tmp)
                ret.append(S)
    return ret


def main():
    N = int(input())
    ret = run(N)
    print(ret[0])
    if len(ret) > 1:
        k = ret[1]
        print(k)
        for s in ret[2]:
            s = [str(si) for si in s]
            print(' '.join(s))


if __name__ == '__main__':
    main()
