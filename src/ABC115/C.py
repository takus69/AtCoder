def run(N, K, h):
    h = sorted(h)
    diff = [h[i+1] - h[i] for i in range(N-1)]
    diff_all = max(h) - min(h)
    r_diff_sum = [0]
    for d in diff:
        r_diff_sum.append(r_diff_sum[-1] + d)
    l_diff_sum = [0]
    for d in reversed(diff):
        l_diff_sum.append(l_diff_sum[-1] + d)
    ret = diff_all
    # 右から何個を除外するか
    for i in range(N - K + 1):
        ret = min(ret, diff_all - r_diff_sum[i] - l_diff_sum[N - K - i])
    return ret


def main():
    N, K = map(int, input().split())
    h = []
    for _ in range(N):
        h.append(int(input()))
    print(run(N, K, h))


if __name__ == '__main__':
    main()
