def run(N, T, A, H):
    ret = 0
    diff = 999
    for i in range(len(H)):
        tmp = T - H[i]*0.006
        if diff > abs(tmp - A):
            ret = i+1
            diff = abs(tmp - A)
    return ret


def main():
    N = int(input())
    T, A= map(int, input().split())
    H = list(map(int, input().split()))
    print(run(N, T, A, H))


if __name__ == '__main__':
    main()
