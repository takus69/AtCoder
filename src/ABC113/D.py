def run(H, W, K):
    # あみだくじの通る道のパターン
    f_h = {(1, 0): 0}
    f_w = {(1, 0): 1}
    for w in range(2, W+1):
        f_h[(w, 0)] = 0
        f_w[(w, 0)] = 0
    for h in range(1, H+1):
        for w in range(1, W+1):
            f_h[(w, h)] = f_h[(w, h-1)] + f_w[(w, h-1)]
        for w in range(1, W+1):
            if w - 1 == 0:
                f_w[(w, h)] = f_h[(w+1, h)]
            elif w + 1 == W+1:
                f_w[(w, h)] = f_h[(w-1, h)]
            else:
                f_w[(w, h)] = f_h[(w+1, h)] + f_h[(w-1, h)]
    # あみだのKに行くための経路の合計
    print(f_h[K, H] + f_w[K, H])
    print(f_h)
    print(f_w)
    return (f_h, f_w)


def main():
    H, W, K = map(int, input().split())
    print(run(H, W, K))


if __name__ == '__main__':
    main()
