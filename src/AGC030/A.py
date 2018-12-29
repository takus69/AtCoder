def run(A, B, C):
    if C > A + B:
        C = A + B + 1
    return B + C


def main():
    A, B, C = map(int, input().split())
    print(run(A, B, C))


if __name__ == '__main__':
    main()
