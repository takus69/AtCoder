def run(T, X):
    return T / X


def main():
    T, X = map(int, input().split())
    print(run(T, X))


if __name__ == '__main__':
    main()
