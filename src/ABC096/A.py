def run(a, b):
    if a <= b:
        return a
    else:
        return a - 1

def main():
    a, b, = map(int, input().split())
    print(run(a, b))


if __name__ == '__main__':
    main()
