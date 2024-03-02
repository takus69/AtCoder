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
        self._size = 1 << self._log
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
            self._update(p >> i)
    
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
        print(self._d)
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

N, Q, = map(int, input().split())
A = list(map(int, input().split()))

def e():
    return {-1: 1, 0: 1}

def op(a1, a2):
    print('a1', a1)
    tmp = {}
    for k, v in a1.items():
        tmp = tmp.get(k, 0) + v
    for k, v in a2.items():
        tmp = tmp.get(k, 0) + v
    tmp = sorted(tmp.items(), key=lambda x: x[0], reverse=True)
    return {tmp[0][0]: tmp[0][1], tmp[1][0]: tmp[1][1]}

sg = SegTree(op, e, N)
for i in range(N):
    sg.set(i, A[i])

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        p = q[1]-1
        x = q[2]
        sg.set(p, x)
    else:
        l = q[1]-1
        r = q[2]-1
        ans = sg.prod(l, r)
        print(ans)

        
        
