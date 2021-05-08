def run(N, A):
    '''
    Aの組合せの和で200で割った余りが同じものが複数あればYes
    組合せのパターンが200個以上あれば、必ずYesとなる
    2^8=256よりNが8以上ならYesになるはず
    '''
    d = {}
    ans = None
    # 1個のパターン
    for i in range(N):
        key = A[i] % 200
        if key in d.keys():
            ans = ((d[key], [i]))
            break
        else:
            d[key] = [i]
    # print(d, ans)
    # 2個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                key = (A[i] + A[j]) % 200
                # print(key)
                if key in d.keys():
                    ans = (d[key], [i, j])
                    break
                else:
                    d[key] = [i, j]
    # print(d)
    # 3個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    key = (A[i] + A[j] + A[k]) % 200
                    if key in d.keys():
                        ans = (d[key], [i, j, k])
                        break
                    else:
                        d[key] = [i, j, k]
    # print(d)
    # 4個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        key = (A[i] + A[j] + A[k] + A[l]) % 200
                        if key in d.keys():
                            ans = (d[key], [i, j, k, l])
                            break
                        else:
                            d[key] = [i, j, k, l]
    # print(d)
    # 5個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            key = (A[i] + A[j] + A[k] + A[l] + A[m]) % 200
                            if key in d.keys():
                                ans = (d[key], [i, j, k, l, m])
                                break
                            else:
                                d[key] = [i, j, k, l, m]
    # 6個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            for n in range(m+1, N):
                                key = (A[i] + A[j] + A[k] + A[l] + A[m] + A[n]) % 200
                                if key in d.keys():
                                    ans = (d[key], [i, j, k, l, m, n])
                                    break
                                else:
                                    d[key] = [i, j, k, l, m, n]
    # 7個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            for n in range(m+1, N):
                                for o in range(n+1, N):
                                    key = (A[i] + A[j] + A[k] + A[l] + A[m] + A[n] + A[o]) % 200
                                    if key in d.keys():
                                        ans = (d[key], [i, j, k, l, m, n, o])
                                        break
                                    else:
                                        d[key] = [i, j, k, l, m, n, o]
    # 8個のパターン
    if ans is None:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    for l in range(k+1, N):
                        for m in range(l+1, N):
                            for n in range(m+1, N):
                                for o in range(n+1, N):
                                    for p in range(o+1, N):
                                        key = (A[i] + A[j] + A[k] + A[l] + A[m] + A[n] + A[o] + A[p]) % 200
                                        if key in d.keys():
                                            ans = (d[key], [i, j, k, l, m, n, o, p])
                                            break
                                        else:
                                            d[key] = [i, j, k, l, m, n, o, p]
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = run(N, A)
    if ans is None:
        print('No')
    else:
        print('Yes')
        print(len(ans[0]), ' '.join(map(str, [i+1 for i in ans[0]])))
        print(len(ans[1]), ' '.join(map(str, [i+1 for i in ans[1]])))



if __name__ == '__main__':
    main()
