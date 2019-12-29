def run(N, S, T):
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    return ans


def main():
    N = int(input())
    S, T = input().split()
    print(run(N, S, T))


if __name__ == '__main__':
    main()
