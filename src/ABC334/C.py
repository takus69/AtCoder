N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if K == 1:
    ans = 0
elif K % 2 == 1:
    sum_diff = 0
    for i in range(1, K, 2):
        sum_diff += A[i+1] - A[i]
    min_diff = sum_diff
    del_i = 0
    tmp_diff = sum_diff
    for i in range(2, K, 2):
        tmp_diff -= A[i] - A[i-1]
        tmp_diff += A[i-1] - A[i-2]
        if min_diff > tmp_diff:
            min_diff = tmp_diff
            del_i = i
    # print('del_i', min_diff, del_i)
    # print(A)
    for j in list(range(0, del_i, 2)) + list(range(del_i+1, K, 2)):
        # print(list(range(0, del_i, 2)) + list(range(del_i+1, K-1, 2)))
        ans += A[j+1]-A[j]
else:
    for i in range(K//2):
        ans += A[2*i+1] - A[2*i]

print(ans)
