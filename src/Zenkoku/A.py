def run(N, A, B):
    min_ = A + B - N
    if min_ < 0:
        min_ = 0
    return '{} {}'.format(min(A, B), min_)


def main():
    N, A, B = list(map(int, input().split()))
    print(run(N, A, B))


if __name__ == '__main__':
    main()
