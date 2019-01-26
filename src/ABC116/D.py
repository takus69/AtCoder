def run(N, K, t, d):
    '''
    おいしさ(d)の昇順でソートする O(NlogN)
    おいしさが大きいもののK個の合計を取得 O(K)
    K個のうちおいしさが少ないものから順にネタの種類が
    増えるように変更していく O(K)
    ネタの種類のうち最大の物の値とインデックスを取得しておく O(K)
    ネタの種類を変えた合計のうち最大のものが答え
    '''
    t_dic = dict(zip(range(N), t))
    d_dic = dict(zip(range(N), d))
    d_dic_sorted = sorted(d_dic.items(), key=lambda x: x[1], reverse=True)
    d_dic_sorted_i = [dd[0] for dd in d_dic_sorted]
    d_dic_sorted_d = [dd[1] for dd in d_dic_sorted]
    d_sum = sum(d_dic_sorted_d[:K])
    t_used = {}
    t_cnt = 0
    for i in t:
        t_used[i] = 0
    for i in d_dic_sorted_i[:K]:
        t_used[t_dic[i]] += 1
        if t_used[t_dic[i]] == 1:
            t_cnt += 1
    t_sum = t_cnt ** 2
    max_sum = d_sum + t_sum
    del_list = d_dic_sorted_i[:K]
    for i in d_dic_sorted_i[K:]:
        di = d_dic[i]
        ti = t_dic[i]
        # ネタの種類が増えるように追加
        if t_used[ti] == 0:
            t_used[ti] += 1
            t_cnt += 1
            t_sum += 2*t_cnt - 1
            d_sum += di
            # ネタが重複しているものを削除
            flg = True
            while len(del_list) > 0 and flg:
                del_i = del_list.pop()
                del_di = d_dic[del_i]
                del_ti = t_dic[del_i]
                if t_used[del_ti] > 1:
                    t_used[del_ti] -= 1
                    d_sum -= del_di
                    max_sum = max(max_sum, d_sum + t_sum)
                    flg = False
    return max_sum


def main():
    N, K = map(int, input().split())
    t = []
    d = []
    for _ in range(N):
        ti, di = map(int, input().split())
        t.append(ti)
        d.append(di)
    print(run(N, K, t, d))


if __name__ == '__main__':
    main()
