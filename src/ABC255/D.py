from bisect import bisect_right


N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
A = sorted(A)
sum_A = []
tmp = 0
for a in A:
    tmp += a
    sum_A.append(tmp)
# print(A)
# print(sum_A)
for _ in range(Q):
    X = int(input())
    i = bisect_right(A, X)  # Xより大きいインデックスを返却
    ans = 0
    # print(i-1, sum_A[i-1], N-i+1, sum_A[-1], X)
    ans += X*(i-1) - sum_A[i-1]  # X以下Aは加算をする分の差分を取得
    if i <= N:  # i==Nの場合はXより大きい値がないため、処理不要
        ans += sum_A[-1] - sum_A[i-1] - X*(N-i+1)
    print(ans)
