def run(m):
    if m < 100:
        return '00'
    elif m <= 5000:
        ret = m / 100
        return '{0:02d}'.format(int(ret))
    elif m <= 30000:
        return '{}'.format(int(m / 1000 + 50))
    elif m <= 70000:
        return '{}'.format(int((m / 1000 - 30) / 5 + 80))
    else:
        return '89'
    return m


def main():
    m = int(input())
    print(run(m))


if __name__ == '__main__':
    main()
