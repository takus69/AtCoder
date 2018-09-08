def run(h, w, a):
    move = []
    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                if a[i][j] % 2 == 1:
                    if j < w-1:
                        move.append([i+1, j+1, i+1, j+2])
                        a[i][j] -= 1
                        a[i][j+1] += 1
                    elif i < h-1:
                        move.append([i+1, j+1, i+2, j+1])
                        a[i][j] -= 1
                        a[i+1][j] += 1
        else:
            for j in range(w-1, -1, -1):
                if a[i][j] % 2 == 1:
                    if j > 0:
                        move.append([i+1, j+1, i+1, j])
                        a[i][j] -= 1
                        a[i][j-1] += 1
                    elif i < h-1:
                        move.append([i+1, j+1, i+2, j+1])
                        a[i][j] -= 1
                        a[i+1][j] += 1
    return move


def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    move = run(h, w, a)
    print(len(move))
    for mv in move:
        mv = map(str, mv)
        print(' '.join(mv))


if __name__ == '__main__':
    main()
