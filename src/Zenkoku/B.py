def run(N, A, B, C):
    ret = 0
    for i in range(N):
        if A[i] == B[i] and B[i] != C[i]:
            ret += 1
        elif A[i] != B[i] and B[i] == C[i]:
            ret += 1
        elif A[i] == C[i] and A[i] != B[i]:
            ret += 1
        elif A[i] == B[i] and B[i] == C[i]:
            pass
        else:
            ret += 2
    return ret


def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    print(run(N, A, B, C))


if __name__ == '__main__':
    main()
