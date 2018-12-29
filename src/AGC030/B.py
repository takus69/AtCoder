def run(L, N, X):
    X = [0] + X
    r = -1
    l = 1
    i = 0
    ret = 0
    dr = 0
    dl = 0
    while l != len(X) + r:
        if i < 0:
            dr = X[i] - X[r]
            dl = L - X[i] + X[l]
        else:
            dr = L - X[r] + X[i]
            dl = X[l] - X[i]
        if i % 2 == 0:
            ret += dr
            i = r
            r -= 1
            if r <= -len(X):
                r = -len(X)
        else:
            ret += dl
            i = l
            l += 1
            if l >= len(X):
                l = 0
    if i < 0:
        dr = X[i] - X[r]
        dl = L - X[i] + X[l]
    else:
        dr = L - X[r] + X[i]
        dl = X[l] - X[i]
    r = -1
    l = 1
    i = 0
    ret2 = 0
    dr = 0
    dl = 0
    while l != len(X) + r:
        if i < 0:
            dr = X[i] - X[r]
            dl = L - X[i] + X[l]
        else:
            dr = L - X[r] + X[i]
            dl = X[l] - X[i]
        if i % 2 == 1:
            ret2 += dr
            i = r
            r -= 1
            if r <= -len(X):
                r = -len(X)
        else:
            ret2 += dl
            i = l
            l += 1
            if l >= len(X):
                l = 0
    if i < 0:
        dr = X[i] - X[r]
        dl = L - X[i] + X[l]
    else:
        dr = L - X[r] + X[i]
        dl = X[l] - X[i]
    ret2 += max(dr, dl)
    return max(ret, ret2)


def main():
    L, N = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(int(input()))
    print(run(L, N, X))


if __name__ == '__main__':
    main()
