from collections import Counter

K = int(input())
T = input()
A = input()

T_cnt = Counter(list(T))
A_cnt = Counter(list(A))
C_cnt = Counter(list(T)+list(A))
cnt = 0
cnt_all = 0
T_score = sum([i*10**(T_cnt[str(i)]) for i in range(1, 10)])
A_score = sum([i*10**(A_cnt[str(i)]) for i in range(1, 10)])
for i in range(1, 10):
    for j in range(1, 10):
        i_cnt = C_cnt[str(i)]
        j_cnt = C_cnt[str(j)]
        if i_cnt == K or j_cnt == K or (i==j and i_cnt == K-1):
            continue
        if i == j:
            cnt_up = (K-i_cnt)*(K-i_cnt-1)
        else:
            cnt_up = (K-i_cnt)*(K-j_cnt)
        cnt_all += cnt_up
        T_tmp = T_score - i*10**(T_cnt[str(i)]) + i*10**(T_cnt[str(i)]+1)
        A_tmp = A_score - j*10**(A_cnt[str(j)]) + j*10**(A_cnt[str(j)]+1)
        # print(i, j, T_tmp, A_tmp, cnt_up)
        if T_tmp > A_tmp:
            cnt += cnt_up
# print(cnt, cnt_all)
print(cnt/cnt_all)
