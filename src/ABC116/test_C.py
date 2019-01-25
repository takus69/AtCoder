import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, [1, 2, 2, 1]), 2)
        self.assertEqual(run(5, [3, 1, 2, 3, 1]), 5)
        self.assertEqual(run(8, [4, 23, 75, 0, 23, 96, 50, 100]), 221)


if __name__ == '__main__':
    unittest.main()
