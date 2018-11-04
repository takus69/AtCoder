def run(N, M, PY):
    PY = sorted(PY, key=lambda x: x[1])
    # key: P, values:list(識別番号, 順番), count
    ret = {}
    for i in range(len(PY)):
        P = PY[i][0]
        j = PY[i][2]
        if P in ret.keys():
            cnt = ret[P][1]
        else:
            cnt = 0
            ret[P] = [[], cnt]
        cnt += 1
        id = '{0:06d}'.format(P)+'{0:06d}'.format(cnt)
        ret[P][0].append([id, j])
        ret[P][1] += 1
    ret2 = []
    for r in ret.values():
        for id, j in r[0]:
            ret2.append([id, j])
    ret2 = sorted(ret2, key=lambda x: x[1])
    ret3 = []
    for r in ret2:
        ret3.append(r[0])
    return ret3


def main():
    N, M = map(int, input().split())
    PY = []
    for i in range(M):
        tmp = list(map(int, input().split()))
        tmp.append(i)
        PY.append(tmp)
    ret = run(N, M, PY)
    for r in ret:
        print(r)


if __name__ == '__main__':
    main()
