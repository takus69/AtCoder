def run(S):
    if len(S) == 2:
        return S
    else:
        return S[::-1]


def main():
    S = input()
    print(run(S))


if __name__ == '__main__':
    main()
