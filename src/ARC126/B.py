'''
同じ点から開始していれば、もう一点が近い方のみを採用
aをソートすれば、bの最長増加部分列(LIS)を求める問題
a1 < a2 ならば、b1 < b2のとき交差しないため、b1 < b2の最長の長さが答えになる
'''
import bisect

N, M = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(list(map(int, input().split())))
# aが同じ点から開始していれば、もう一点が近い方のみを採用
ab = sorted(ab, key=lambda x: (x[0], x[1]))
ab1 = [ab[0]]
b = [ab[0][1]]
for i in range(1, M):
    if ab1[-1][0] == ab[i][0]:
        continue
    ab1.append(ab[i])
    b.append(ab[i][1])

dp = [max(b)+1] * len(b)  # LIS用のDP: 最長部分増加列で長さjの時、右端に選択される値の最小値
for i in range(len(b)):
    j = bisect.bisect_right(dp, b[i])  # 同じ値だと伸ばす方向
    dp[j] = min(dp[j], b[i])
ans = max([j+1 for j in range(len(b)) if dp[j] < max(b)+1])
# print([j+1 for j in range(len(b)) if dp[j] < max(b)+1])
# print('dp', dp)
# print('ab', ab)
# print('b', b)
print(ans)
