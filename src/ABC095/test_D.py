import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 20, [[2, 80], [9, 120], [16, 1]]), 191)
        self.assertEqual(run(3, 20, [[2, 80], [9, 1], [16, 120]]), 192)
        self.assertEqual(run(1, 100000000000000, [[50000000000000, 1]]), 0)
        self.assertEqual(run(15, 10000000000, [[400000000, 1000000000],
                         [800000000, 1000000000], [1900000000, 1000000000],
                         [2400000000, 1000000000], [2900000000, 1000000000],
                         [3300000000, 1000000000], [3700000000, 1000000000],
                         [3800000000, 1000000000], [4000000000, 1000000000],
                         [4100000000, 1000000000], [5200000000, 1000000000],
                         [6600000000, 1000000000], [8000000000, 1000000000],
                         [9300000000, 1000000000], [9700000000, 1000000000]]))


if __name__ == '__main__':
    unittest.main()
