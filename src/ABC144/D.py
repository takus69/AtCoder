import math


def run(a, b, x):
    if a*a*b >= 2*x:
        tan = a * (b**2) / (2*x)
    else:
        tan = (2*b) / a - ((2*x) / a**3)
    ret = math.degrees(math.atan(tan))
    return ret


def main():
    a, b, x = map(int, input().split())
    print(run(a, b, x))


if __name__ == '__main__':
    main()
