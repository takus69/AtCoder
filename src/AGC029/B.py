import collections


def run(N, A):
    cnt = 0
    beki = [2**i for i in range(1, 32)]
    A = sorted(A, reverse=True)
    used = collections.Counter(A)
    for a in A:
        if used[a] == 0:
            continue
        used[a] -= 1
        while beki[-1] > 2*a:
            beki.pop(-1)
        if used[beki[-1] - a] >= 1:
            cnt += 1
            used[beki[-1] - a] -= 1
    return cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(run(N, A))


if __name__ == '__main__':
    main()
