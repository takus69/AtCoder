def run(S):
    ret = 753 - 111
    for i in range(len(str(S)) - 2):
        ret = min(ret, abs(753 - int(str(S)[i:i+3])))
    return ret


def main():
    S = input()
    print(run(S))


if __name__ == '__main__':
    main()
