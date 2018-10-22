def run(N, S):
    ret = 0
    for i in range(1, N-1):
       ret = max([ret, num_dup(N, S, i)])
    return ret


def num_dup(N, S, x):
    '''
    0 < x < N-1
    '''
    s1 = list(set(S[:x]))
    s2 = list(set(S[x:]))
    cnt = 0
    for ss in s1:
        if ss in s2:
            cnt += 1
    return cnt

def main():
    N = int(input())
    S = input()
    print(run(N, S))


if __name__ == '__main__':
    main()
