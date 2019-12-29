def run(A, B):
    ans = None
    if 1 not in [A, B]:
        ans = 1
    if 2 not in [A, B]:
        ans = 2
    if 3 not in [A, B]:
        ans = 3
    return ans


def main():
    A = int(input())
    B = int(input())
    print(run(A, B))


if __name__ == '__main__':
    main()
