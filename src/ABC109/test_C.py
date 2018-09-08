import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 3, [1, 7, 11]), 2)
        self.assertEqual(run(3, 81, [33, 105, 57]), 24)
        self.assertEqual(run(1, 1, [1000000000]), 999999999)
        self.assertEqual(run(2, 1, [7, 16]), 3)
        self.assertEqual(run(3, 1, [31, 67, 112]), 3)


if __name__ == '__main__':
    unittest.main()
