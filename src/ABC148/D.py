def run(N, a):
    ans = -1
    cnt = 0
    idx = 0
    i = 1
    match = False
    while idx < N:
        ai = a[idx]
        idx += 1
        if ai == i:
            # print('match', i, ai, idx)
            match = True
            i += 1
        else:
            # print('break', i, ai, idx)
            cnt += 1
    if match:
        ans = cnt
    return ans


def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(run(N, a))


if __name__ == '__main__':
    main()
