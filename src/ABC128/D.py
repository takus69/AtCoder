def run(N, K, V):
    ret = 0
    for L_get in range(K+1):
        for R_get in range(K-L_get+1):
            if L_get + R_get > N:
                break
            for Leave in range(K-L_get-R_get+1):
                if Leave > L_get + R_get:
                    break
                if L_get == 0:
                    L_lists = []
                else:
                    L_lists = V[:L_get]
                if R_get == 0:
                    R_lists = []
                else:
                    R_lists = V[-R_get:]
                lists = L_lists + R_lists
                sorted_lists = sorted(lists)
                ret = max(ret, sum(lists) - sum(sorted_lists[:Leave]))
    return ret


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    print(run(N, K, V))


if __name__ == '__main__':
    main()
