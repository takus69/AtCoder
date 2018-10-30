def run(s, K):
    sub_list = []
    for i in range(len(s)):
        for j in range(i, i+K):
            if j+1 > len(s):
                break
            sub_list.append(s[i:j+1])
    sub_list = sorted(set(sub_list))
    return sub_list[K-1]


def main():
    s = input()
    K = int(input())
    print(run(s, K))


if __name__ == '__main__':
    main()
