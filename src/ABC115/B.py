def run(N, p):
    return int(sum(p) - max(p) / 2)


def main():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(int(input()))
    print(run(N, p))


if __name__ == '__main__':
    main()
