import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [2, 1, 2]), 1)
        self.assertEqual(run(3, [2, 2, 2]), -1)
        self.assertEqual(run(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), 7)
        self.assertEqual(run(1, [1]), 0)


if __name__ == '__main__':
    unittest.main()
