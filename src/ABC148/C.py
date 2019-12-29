import fractions


def run(A, B):
    return A * B // fractions.gcd(A, B)


def main():
    A, B = map(int, input().split())
    print(run(A, B))


if __name__ == '__main__':
    main()
