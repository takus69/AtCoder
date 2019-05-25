def run(N, L):
    L = sorted(L)
    ret = 'No'
    if 2*L[-1] < sum(L):
        ret = 'Yes'
    return ret


def main():
    N = int(input())
    L = list(map(int, input().split()))
    print(run(N, L))


if __name__ == '__main__':
    main()
