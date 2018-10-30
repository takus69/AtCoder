def run(N):
    # 素数のリストを作成
    p = [2]
    for i in range(3, 55555):
        flag = True
        for pp in p:
            if i % pp == 0:
                flag = False
                continue
        if flag:
            p.append(i)
    return p


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()
