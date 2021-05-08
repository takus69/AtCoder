def run(N, A):
    '''
    Ai - Aj が200の倍数になるには以下の条件が必要
    - 200で割った余りが同じ
    '''
    u2 = {}
    for i in range(N):
        key = A[i] % 200
        u2[key] = u2.get(key, 0) + 1
    ans = 0
    # print(u2)
    for key in u2.keys():
        tmp = u2[key]
        # print(key, tmp)
        if tmp > 1:
            ans += tmp * (tmp-1) // 2
    return ans

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(run(N, A))


if __name__ == '__main__':
    main()
