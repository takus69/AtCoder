def run(N, M, A):
    A = sorted(A, reverse=True)
    n1 = M // 3
    n2 = M % 3
    ans = 0
    for i in range(n1):
        tmp_ans = 4*sum(A[:n1-i]) + 2*sum(A[1:n1-i+1])
        if n2 == 1:
            tmp_ans += 2 * A[n1-i+1]
        elif n2 == 2:
            tmp_ans += 3 * A[n1-i+1] + A[n1-i+2]
        ans = max(ans, tmp_ans)
    return ans


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(run(N, M, A))


if __name__ == '__main__':
    main()
