def run(N, K, V):
    ret = 0
    L_cal = {(0, 0): 0}
    R_cal = {(0, 0): 0}
    for L_get in range(1, K+1):
        lists = V[:L_get]
        sorted_lists = sorted(lists)
        sum_lists = sum(lists)
        for L_set in range(L_get+1):
            L_cal[(L_get, L_set)] = sum_lists - sum(sorted_lists[:L_set])
    for R_get in range(1, K+1):
        lists = V[-R_get:]
        sorted_lists = sorted(lists)
        sum_lists = sum(lists)
        for R_set in range(R_get+1):
            R_cal[(R_get, R_set)] = sum_lists - sum(sorted_lists[:R_set])
    for L_K in range(K+1):
        R_K = K - L_K
        for L_get in range(L_K+1):
            L_set = L_K - L_get
            for R_get in range(R_K+1):
                R_set = R_K - R_get
                if L_set <= L_get and R_set <= R_get:
                    ret = max(ret, L_cal[(L_get, L_set)]+R_cal[(R_get, R_set)])
    return ret


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    print(run(N, K, V))


if __name__ == '__main__':
    main()
