def run(N, K, A):
    ret = 0
    for i in range(K+1):
        ret = max(xxor(i, A), ret)
    return ret


def xxor(X, A):
    ret = 0
    for i in range(len(A)):
        ret += X ^ A[i]
    return ret


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(run(N, K, A))


if __name__ == '__main__':
    main()
