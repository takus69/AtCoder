def run(n, k, x):
    # ri = 0
    # li = k-1
    # if n == 1:
    #    return x[0]
    # x2 = x
    ret = abs(x[0]) + abs(x[0] - x[k-1])
    for i in range(n-k+1):
        ri = i
        li = i + k - 1
        tmp = min(abs(x[ri]) + abs(x[ri] - x[li]),
                  abs(x[li]) + abs(x[ri] - x[li]))
        ret = min(ret, tmp)
        '''
        if x[ri] > x[i]:
        elif x[ri] == x[i]:
            if x[ri+1] < x[i-1]:
                ri = i-k+1
                li = i
        else:
            if x2[li] <= 0:
                return x[ri]
            elif x2[ri] >= 0:
                return x[li]
            elif x[ri] > x[li]:
                return x[ri] + 2*x[li]
            else:
                return 2*x[ri] + x[li]
    if x2[li] <= 0:
        return x[ri]
    elif x2[ri] >= 0:
        return x[li]
    elif x[ri] > x[li]:
        return x[ri] + 2*x[li]
    else:
        return 2*x[ri] + x[li]
        '''
    return ret


def read_line():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    return (n, k, x)


def main():
    n, k, x = read_line()
    print(run(n, k, x))


if __name__ == '__main__':
    main()
