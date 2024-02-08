from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0]*n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p-1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r-1]
            r -= r & -r
        return s

max_A = max(A)
fw1 = FenwickTree(max_A+1)  # fw1[i] = (A[j]==iの個数)
fw2 = FenwickTree(max_A+1)  # fw2[i] = (A[j]==iの個数)*i

ans = 0
for i in range(N):
    K = i+1
    # 分母
    bunbo = pow(K*K, -1, MOD)

    # 分子
    ans += 2*(fw1.sum(0, A[i]+1)*A[i] + fw2.sum(A[i]+1, max_A+1)) + A[i]
    # print('fw', fw1.sum(0, A[i]+1), fw2.sum(A[i]+1, max_A+1))
    # print(ans, bunbo)
    ans %= MOD
    print((ans*bunbo)%MOD)
    fw1.add(A[i], 1)
    fw2.add(A[i], A[i])


'''
ans = 0
sl = SortedList([])
cnt = {}
sum_A = 0
for i in range(N):
    # 分母を求める
    K = i+1
    bunbo = pow(K*K, -1, MOD)

    # 分子を求める
    # Aをソートすると、i+1番目において、A[i]*(1+2*i)の和が分子(1の部分は重複がある場合は考慮が必要)
    ai = A[i]
    sl.add(ai)
    sum_A += ai
    cnt_i = cnt.get(ai, 0)+1
    cnt[ai] = cnt_i
    j = sl.bisect_left(ai)
    # print('j', j)
    ans += (ai * (2*cnt_i-1 + 2*j)) % MOD  # 2*cnt_iは同じ値がある場合、一つは決まっているので残りのcnt_iとの組み合わせを逆含めて足すが、自分自身の組み合わせは1つのため-1している
    ans += 2*sum(sl[j+cnt_i:])  # jより後の累積和を2倍して足す
    # print('i', i, A[i], (1+2*i))
    ans %= MOD
    # print('debug', K, ans, bunbo)
    print((ans*bunbo)%MOD)
'''
