

def run(a, b):
    if a > 8 or b > 8:
        return ':('
    else:
        return 'Yay!'


def read_line():
    a, b = input().split()
    a = int(a)
    b = int(b)
    return (a, b)


def main():
    a, b = read_line()
    print(run(a, b))


if __name__ == '__main__':
    main()
