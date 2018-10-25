import math


def run(X):
    ret = 1
    for i in range(2, X):
        for j in range(2, int(math.log2(X))):
            tmp = i**j
            if tmp > X:
                break
            ret = max(ret, tmp)
    return ret


def main():
    X = int(input())
    print(run(X))


if __name__ == '__main__':
    main()
