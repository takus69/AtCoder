import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 3, [10, 15, 11, 14, 12]), 2)
        self.assertEqual(run(5, 3, [5, 7, 5, 7, 7]), 0)


if __name__ == '__main__':
    unittest.main()
