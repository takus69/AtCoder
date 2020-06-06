degit = [
    ['###', '#.#', '#.#', '#.#', '###'],
    ['.#.', '##.', '.#.', '.#.', '###'],
    ['###', '..#', '###', '#..', '###'],
    ['###', '..#', '###', '..#', '###'],
    ['#.#', '#.#', '###', '..#', '..#'],
    ['###', '#..', '###', '..#', '###'],
    ['###', '#..', '###', '#.#', '###'],
    ['###', '..#', '..#', '..#', '..#'],
    ['###', '#.#', '###', '#.#', '###'],
    ['###', '#.#', '###', '..#', '###'],
]


def main():
    N = int(input())
    s = []
    for i in range(5):
        s.append(input())

    ans = []
    for i in range(N):
        target_s = []
        for j in range(5):
            target_s.append(s[j][4*i+1:4*i+4])
        ans.append(check_degit(target_s))

    print(''.join(map(str, ans)))


def check_degit(s5x3):
    for i in range(10):
        s_d = degit[i]
        flg = True
        for j in range(5):
            if s5x3[j] != s_d[j]:
                flg = False
                break
        if flg:
            d = i
            break
    return d


if __name__ == '__main__':
    main()
