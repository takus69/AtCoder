import unittest

from D import UnionFind


class TestSample(unittest.TestCase):
    def test_run(self):
        obj = UnionFind()
        self.assertEqual(obj.run(5, 2, [5, 3, 1, 4, 2], [[1, 3], [5, 4]]), 2)
        self.assertEqual(obj.run(3, 2, [3, 2, 1], [[1, 2], [2, 3]]), 3)
        self.assertEqual(obj.run(10, 8, [5, 3, 6, 8, 7, 10, 9, 1, 2, 4], [[3, 1], [4, 1], [5, 9], [2, 5], [6, 5], [3, 5], [8, 9], [7, 9]]), 8)
        self.assertEqual(obj.run(5, 1, [1, 2, 3, 4, 5], [[1, 5]]), 5)


if __name__ == '__main__':
    unittest.main()
