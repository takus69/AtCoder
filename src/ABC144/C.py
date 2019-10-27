def run(N):
    lists = [N-1]
    for i in range(2, int(N**(1/2))+1):
        if N % i == 0:
            lists.append(i + (N // i) - 2)
    return min(lists)


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
