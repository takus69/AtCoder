def run(N, S):
    num_l = [0]
    num_r = [0]
    for i in range(1, len(S)):
        cnt = num_l[i-1]
        if S[i-1] == 'W':
            num_l.append(cnt+1)
        else:
            num_l.append(cnt)
        cnt = num_r[i-1]
        if S[N-i] == 'E':
            num_r.append(cnt+1)
        else:
            num_r.append(cnt)
    ret = max(num_l) + max(num_r)
    for i in range(len(num_l)):
        ret = min(ret, num_l[i]+num_r[N-1-i])
    return ret


def main():
    N = int(input())
    S = input()
    print(run(N, S))


if __name__ == '__main__':
    main()
