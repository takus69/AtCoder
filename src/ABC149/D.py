def run(N, K, R, S, P, T):
    ans = 0
    main = ''
    for i in range(len(T)):
        t = T[i]
        if i < K:
            if t == 'r':
                ans += P
                main += 'p'
            elif t == 's':
                ans += R
                main += 'r'
            elif t == 'p':
                ans += S
                main += 's'
        else:
            pre_t = main[i - K]
            if t == 'r' and pre_t != 'p':
                ans += P
                main += 'p'
            elif t == 's' and pre_t != 'r':
                ans += R
                main += 'r'
            elif t == 'p' and pre_t != 's':
                ans += S
                main += 's'
            else:
                main += ' '
    return ans


def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    print(run(N, K, R, S, P, T))


if __name__ == '__main__':
    main()
