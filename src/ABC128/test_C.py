import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 2, [2, 1], [[1, 2], [2]], [0, 1]), 1)
        self.assertEqual(run(2, 3, [2, 1, 1], [[1, 2], [1], [2]], [0, 0, 1]), 0)
        self.assertEqual(run(5, 2, [3, 2], [[1, 2, 5], [2, 3]], [1, 0]), 8)


if __name__ == '__main__':
    unittest.main()
