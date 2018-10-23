def run(N, A):
    r = 0
    A_sum = 0
    A_xor = 0
    A_and = 0
    r = -1
    cnt = 0
    for l in range(N):
        while (A_sum - A_xor == 2*A_and) or r < N:
            r += 1
            A_sum += A[r]
            A_xor ^= A[r]
            A_and &= A[r]
        cnt += r - 1
        '''
        元に戻す
        xor:
        0 0 => 0
        0 1 => 1
        1 0 => 1
        1 1 => 0

        and:
        0 0 => 0 or 1
        0 1 => x
        1 0 => 0
        1 1 => 1
        '''
        A_sum -= A[l]
        A_xor ^= A[l]
        A_and = A[l]
    return cnt


def main():
    N = int(input())
    A = map(int, input().split())
    print(run(N, A))


if __name__ == '__main__':
    main()
