def run(N):
    cnt = 0
    for i in range(3, N+1, 2):
        if not valid(i, 1):
            continue
        if not valid(i, 2):
            continue
        if not valid(i, 3):
            continue
        is3 = False
        is5 = False
        is7 = False
        plus = 1
        for j in range(len(str(i))):
            a = (i // 10**j) % 10
            if a == 3:
                is3 = True
            elif a == 5:
                is5 = True
            elif a == 7:
                is7 = True
            else:
                plus = 0
                continue
        if not is3 or not is5 or not is7:
            plus = 0
        cnt += plus
    return cnt


def valid(n, i):
    a = (n // 10**(i-1)) % 10
    if a == 3 or a == 5 or a == 7:
        return True
    else:
        return False


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
