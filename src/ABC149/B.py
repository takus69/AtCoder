def run(a, b, k):
    ans1 = a - k
    ans2 = b
    if ans1 < 0:
        ans2 = b + ans1
        ans1 = 0
    if ans2 < 0:
        ans2 = 0
    return ans1, ans2


def main():
    a, b, k = map(int, input().split())
    ans = run(a, b, k)
    print(ans[0], ans[1])


if __name__ == '__main__':
    main()
