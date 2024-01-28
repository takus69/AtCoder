'''
同じ点から開始していれば、もう一点が近い方のみを採用 <= サンプル2でNG。前のbと重なると1つ少なくなる
(a, -b)をソートすれば、bの最長増加部分列(LIS)を求める問題
a1 < a2 ならば、b1 < b2のとき交差しないため、b1 < b2の最長の長さが答えになる
'''
import bisect

N, M = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(list(map(int, input().split())))
# aが同じ点から開始していれば、もう一点が近い方のみを採用
ab = sorted(ab, key=lambda x: (x[0], -x[1]))

INF = max([b for a, b in ab])+1
dp = [INF] * M  # LIS用のDP: 最長部分増加列で長さj-1の時、右端に選択される値の最小値
for a, b in ab:
    j = bisect.bisect_left(dp, b)  # 同じ値だと上書き
    dp[j] = min(dp[j], b)
ans = max([j+1 for j in range(M) if dp[j] < INF])
# print('dp', dp)
# print('ab', ab)
# print('b', b)
print(ans)
