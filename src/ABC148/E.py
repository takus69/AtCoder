import math


def run(N):
    if N == 0:
        return 0
    ans = 0
    if N % 2 == 0:
        for i in range(int(math.log(N, 5))):
            ans += N // (10 * (5**i))
    return ans


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
