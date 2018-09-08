def run(n, w):
    for i in range(n-1):
        if w[i] in w[i+1:]:
            return 'No'
        if w[i][len(w[i])-1] != w[i+1][0]:
            return 'No'
    return 'Yes'


def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())
    print(run(n, w))


if __name__ == '__main__':
    main()
