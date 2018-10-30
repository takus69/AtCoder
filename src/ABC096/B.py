def run(A, B, C, K):
    if A > B:
        if A > C:
            ret = A*(2**K) + B + C
        else:
            if B > C:
                ret = B*(2**K) + A + C
            else:
                ret = C*(2**K) + A + B
    else:
        if B > C:
            ret = B*(2**K) + A + C
        else:
            ret = C*(2**K) + A + B
    return ret


def main():
    A, B, C = map(int, input().split())
    K = int(input())
    print(run(A, B, C, K))


if __name__ == '__main__':
    main()
