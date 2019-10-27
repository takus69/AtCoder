def run(N):
    ret = 'No'
    for i in range(1, 10):
        if N % i == 0 and N / i <= 9:
            ret = 'Yes'
    return ret


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
