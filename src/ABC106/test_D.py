import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        n = 2
        m = 3
        qq = 1
        ll = [1, 1, 2]
        r = [1, 2, 2]
        p = [1]
        q = [2]
        self.assertEqual(run(n, m, qq, ll, r, p, q), [3])

        n = 10
        m = 3
        qq = 2
        ll = [1, 2, 7]
        r = [5, 8, 10]
        p = [1, 3]
        q = [7, 10]
        self.assertEqual(run(n, m, qq, ll, r, p, q), [1, 1])


if __name__ == '__main__':
    unittest.main()
