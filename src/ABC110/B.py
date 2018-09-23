def run(N, M, X, Y, x, y):
    x.append(X)
    y.append(Y)
    max_x = max(x)
    min_y = min(y)
    if max_x < min_y:
        ret = 'No War'
    else:
        ret = 'War'
    return ret


def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(run(N, M, X, Y, x, y))


if __name__ == '__main__':
    main()
