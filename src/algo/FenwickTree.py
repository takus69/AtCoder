# reference: https://qiita.com/AkariLuminous/items/f2f7930e7f67963f0493

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
    

if __name__ == '__main__':
    n = 8
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    fw = FenwickTree(n)
    for i, a_i in enumerate(a): fw.add(i, a_i)
    assert fw.sum(2, 4) == sum(a[2:4])
    assert fw.sum(6, 7) == sum(a[6:7])
    fw.add(2, 6)
    a[2] += 6
    fw.add(5, -1)
    a[5] += -1
    assert fw.sum(0, 3) == sum(a[0:3])
    assert fw.sum(3, 7) == sum(a[3:7])
