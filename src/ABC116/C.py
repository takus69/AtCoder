def run(N, h):
    start_flg = False
    ret = 0
    for i in range(max(h)):
        start_flg = False
        for j in range(N):
            if h[j] > 0:
                h[j] -= 1
                if not start_flg:
                    start_flg = True
                    ret += 1
            else:
                start_flg = False
    return ret


def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(run(N, h))


if __name__ == '__main__':
    main()
