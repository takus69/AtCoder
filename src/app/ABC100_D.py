def run(n, m, x, y, z):
    s1 = [x[i] + y[i] + z[i] for i in range(n)]
    s1.sort(reverse=True)
    s2 = [-x[i] + y[i] + z[i] for i in range(n)]
    s2.sort(reverse=True)
    s3 = [x[i] - y[i] + z[i] for i in range(n)]
    s3.sort(reverse=True)
    s4 = [-x[i] - y[i] + z[i] for i in range(n)]
    s4.sort(reverse=True)
    s5 = [x[i] + y[i] - z[i] for i in range(n)]
    s5.sort(reverse=True)
    s6 = [-x[i] + y[i] - z[i] for i in range(n)]
    s6.sort(reverse=True)
    s7 = [x[i] - y[i] - z[i] for i in range(n)]
    s7.sort(reverse=True)
    s8 = [-x[i] - y[i] - z[i] for i in range(n)]
    s8.sort(reverse=True)
    max_sum = sum(s1[0:m])
    tmp_sum = sum(s2[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s3[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s4[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s5[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s6[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s7[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    tmp_sum = sum(s8[0:m])
    if max_sum < tmp_sum:
        max_sum = tmp_sum
    return max_sum


def read_line():
    n, m = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        tx, ty, tz = map(int, input().split())
        x.append(tx)
        y.append(ty)
        z.append(tz)
    return (n, m, x, y, z)


def main():
    n, m, x, y, z = read_line()
    print(run(n, m, x, y, z))


if __name__ == '__main__':
    main()
