def run(A, B, K):
    for i in range(K):
        if i % 2 == 0:
            if A % 2 == 1:
                A -= 1
            A /= 2
            B += A
        else:
            if B % 2 == 1:
                B -= 1
            B /= 2
            A += B
    return '{} {}'.format(int(A), int(B))


def main():
    A, B, K = map(int, input().split())
    print(run(A, B, K))


if __name__ == '__main__':
    main()
