N, K = map(int, input().split())
A = list(map(int, input().split()))


def search_switch_k(N_A, K, A, is_sorted_A):
    for i in range(N):
        a = A[0]
        # print(i, N_A, K, A, is_sorted_A, a, K)
        if a == i+1:
            if K > N_A*(N_A-1)//2+1:
                K -= N_A*(N_A-1)//2+1
            else:
                is_sorted_A[i] = False
                K -= d
                return N_A-1, K, A[1:], is_sorted_A
        elif is_sorted_A[i]:
            K -= 1
        if K == 0:
            # 先頭からi+1までを反転する
            for j in range(N_A):
                if A[j] == i+1:
                    j2 = j
                    break
            switch_A = []
            for j in range(j2, -1, -1):
                switch_A.append(A[j])
            for j in range(j2+1, N_A):
                switch_A.append(A[j])
            is_sorted_A[i] = False
            return N_A, K, switch_A, is_sorted_A

N2, K2 = N, K
switch_A = []
for a in A:
    switch_A.append(a)
is_sorted_A = [True for _ in range(N)]

kk = 0
for i in range(N-1):
    a = A[i]
    for a2 in A[i+1:]:
        if a2 < a:
            kk += 1
# print(kk, K, kk+N-1)
if kk <= K and K <= kk+N-1:
    ans = A
else:
    if K > kk:
        d = 1
    else:
        d = 0
    # print('d:', d)

    ans = []
    while K2 > 0 and N2 > 0:
        # print(ans)
        a = switch_A[0]
        # print('in:', N2, K2, switch_A, is_sorted_A)
        N2, K2, switch_A, is_sorted_A = search_switch_k(N2, K2, switch_A, is_sorted_A)
        # print('out:', N2, K2, switch_A, is_sorted_A)
        if K2 == 0 and N2 > 0:
            ans += switch_A
        else:
            ans.append(a)
        # print(ans)

ans = list(map(str, ans))
print(' '.join(ans))
