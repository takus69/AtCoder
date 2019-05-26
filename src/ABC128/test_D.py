import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(6, 4, [-10, 8, 2, 1, 2, 6]), 14)
        self.assertEqual(run(6, 4, [-6, -100, 50, -2, -5, -3]), 44)
        self.assertEqual(run(6, 3, [-6, -100, 50, -2, -5, -3]), 0)


if __name__ == '__main__':
    unittest.main()
