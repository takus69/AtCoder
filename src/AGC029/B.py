def run(N, A):
    cnt = 0
    beki = [2**i for i in range(1, 32)]
    A = sorted(A, reverse=True)
    for i in len(A):
        for j in 
        tmp1 = []


    return (N, A)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(run(N, A))


if __name__ == '__main__':
    main()
