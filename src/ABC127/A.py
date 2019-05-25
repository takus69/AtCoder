def run(A, B):
    if A >= 13:
        fee = B
    elif A >= 6:
        fee = B / 2
    else:
        fee = 0
    return int(fee)


def main():
    A, B = map(int, input().split())
    print(run(A, B))


if __name__ == '__main__':
    main()
