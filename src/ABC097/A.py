def run(a, b, c, d):
    ret = 'No'
    if abs(a - c) <= d:
        ret = 'Yes'
    elif abs(a - b) <= d and abs(b - c) <= d:
        ret = 'Yes'
    return ret


def main():
    a, b, c, d = map(int, input().split())
    print(run(a, b, c, d))


if __name__ == '__main__':
    main()
