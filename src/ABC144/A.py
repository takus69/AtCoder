def run(A, B):
    ret = A * B
    if A > 9:
        ret = -1
    if B > 9:
        ret = -1
    return ret


def main():
    A, B = map(int, input().split())
    print(run(A, B))


if __name__ == '__main__':
    main()
