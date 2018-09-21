def run(n, X, x):
    ret = 0
    i = n-1
    while i >= 0:
        if i == 0:
            ret += 5*(x[i]) + 2*X
            break
        ret += 5*(x[i] + x[i-1]) + 3*X
        i -= 2
        if i >= 0:
            j = 1
            tmp = 2*j*x[i]
            while tmp < (j)*X:
                ret += (2*(j+2)+1)*x[i] + X
                j += 1
                i -= 1
                if i < 0:
                    break
                tmp = 2*j*x[i]
    return ret


def main():
    n, X = map(int, input().split())
    x = list(map(int, input().split()))
    print(run(n, X, x))


if __name__ == '__main__':
    main()
