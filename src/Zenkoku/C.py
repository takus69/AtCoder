def run(N, A, B):
    sum_AB = {}
    for i in range(N):
        sum_AB[i] = A[i] + B[i]
    sum_AB = sorted(sum_AB.items(), key=lambda x: x[1], reverse=True)
    turn_A = True
    sum_A = 0
    sum_B = 0
    for tmp in sum_AB:
        if turn_A:
            sum_A += A[tmp[0]]
        else:
            sum_B += B[tmp[0]]
        turn_A = not turn_A
    return sum_A - sum_B
    '''
    diff = {}
    for i in range(N):
        diff[i] = A[i] - B[i]
    diff = sorted(diff.items(), key=lambda x: x[1])
    print(diff)
    li = 0
    ri = N - 1
    sum_A = 0
    sum_B = 0
    turn_A = True
    for _ in range(N):
        if -diff[li][1] >= diff[ri][1]:
            if turn_A:
                sum_A += A[li]
            else:
                sum_B += B[li]
            li += 1
        else:
            if turn_A:
                sum_A += A[ri]
            else:
                sum_B += B[ri]
            ri -= 1
        turn_A = not turn_A
    return sum_A - sum_B
    '''


def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        A.append(tmp[0])
        B.append(tmp[1])
    print(run(N, A, B))


if __name__ == '__main__':
    main()
