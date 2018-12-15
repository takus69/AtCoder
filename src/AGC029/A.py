def run(S):
    '''
    Bをすべて右に、Wをすべて左に移動する回数を求める
    '''
    cnt = 0
    n = len(S)
    cnt_B = 0
    cnt_W = 0
    for i in range(len(S)):
        if S[i] == 'B':
            cnt_B += 1
            cnt += n - (i+cnt_B)
        else:
            cnt += i - cnt_W
            cnt_W += 1
    return int(cnt / 2)


def main():
    S = input()
    print(run(S))


if __name__ == '__main__':
    main()
