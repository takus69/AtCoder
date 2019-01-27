def run(D):
    ret = 'Christmas'
    add = ' Eve'
    ret += add * (25 - D)
    return ret


def main():
    D = int(input())
    print(run(D))


if __name__ == '__main__':
    main()
