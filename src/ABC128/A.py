def run(A, P):
    return (A*3 + P)//2


def main():
    A, P = map(int, input().split())
    print(run(A, P))


if __name__ == '__main__':
    main()
