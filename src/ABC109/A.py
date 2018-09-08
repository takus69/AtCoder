def run(a, b):
    if a % 2 == 0 or b % 2 == 0:
        return 'No'
    else:
        return 'Yes'


def main():
    a, b = map(int, input().split())
    print(run(a, b))


if __name__ == '__main__':
    main()
