import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 3, [[0, 1, 1], [1, 0, 1], [1, 4, 0]], [[1, 2], [3, 3]]), 3)
        self.assertEqual(run(4, 3, [[0, 12, 71], [81, 0, 53], [14, 92, 0]], [[1, 1, 2, 1], [2, 1, 1, 2], [2, 2, 1, 3], [1, 1, 2, 2]]), 428)
        self.assertEqual(run(500, 30, [[0]*30]*30, [[1]*500]*500), 0)


if __name__ == '__main__':
    unittest.main()
