class SegTree:
    '''
    n: 要素数
    e: 単位元
    op: 演算
    v: 対象の配列
    '''
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()  # 2^(_log) >= n となる最小の整数
        self._size = 1 << self._log  # 2^_log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)  # p//2 をi回
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

N, Q = map(int, input().split())
A = list(map(int, input().split()))

def e1():
    return 0
sg = SegTree(max, e1, N, A)

ans = []
for _ in range(Q):
    T, q1, q2 = list(map(int, input().split()))
    if T == 1:
        sg.set(q1-1, q2)
    elif T == 2:
        ans.append(sg.prod(q1-1, q2))
    else:
        l, r = q1-1, N
        if sg.prod(l, r) < q2:
            ans.append(N+1)
        else:
            while l+1 < r:
                m = (l+r)//2
                a = sg.prod(l, m)
                if a < q2:
                    l = m
                else:
                    r = m
            ans.append(l+1)

for a in ans:
    print(a)
