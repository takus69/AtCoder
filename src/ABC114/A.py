def run(a):
    ret = 'NO'
    if a == 5 or a == 3 or a == 7:
        ret = 'YES'
    return ret


def main():
    a = int(input())
    print(run(a))


if __name__ == '__main__':
    main()
