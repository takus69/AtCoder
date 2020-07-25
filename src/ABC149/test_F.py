import unittest

from F import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [[1, 2], [2, 3]]), 125000001)
        self.assertEqual(run(4, [[1, 2], [2, 3], [3, 4]]), 375000003)
        self.assertEqual(run(4, [[1, 2], [1, 3], [1, 4]]), 250000002)
        self.assertEqual(run(7, [[4, 7], [3, 1], [2, 6], [5, 2], [7, 1], [2, 7]]), 570312505)


if __name__ == '__main__':
    unittest.main()
