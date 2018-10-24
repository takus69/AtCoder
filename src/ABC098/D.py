def run(N, A):
    r = 0
    A_sum = 0
    A_xor = 0
    A_and = 0
    r = -1
    cnt = 0
    for l in range(N):
        while (A_sum - A_xor == 2*A_and) and r < N-1:
            r += 1
            A_sum += A[r]
            A_xor ^= A[r]
            A_and &= A[r]
        if A_sum - A_xor == 2*A_and:
            cnt += r - l + 1
        else:
            cnt += r - l
        '''
        元に戻す
        xor:
        0 0 => 0
        0 1 => 1
        1 0 => 1
        1 1 => 0
        '''
        A_sum -= A[l]
        A_xor ^= A[l]
        A_and = 2*(A_sum - A_xor)
    return cnt


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(run(N, A))


if __name__ == '__main__':
    main()
