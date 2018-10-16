def run(n):
    ret = 'ABC'
    if n > 999:
        ret = 'ABD'
    return ret


def main():
    n = int(input())
    print(run(n))


if __name__ == '__main__':
    main()
