import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, [3, 8, 5, 1]), 'Yes')
        self.assertEqual(run(4, [3, 8, 4, 1]), 'No')
        self.assertEqual(run(10, [1, 8, 10, 5, 8, 12, 34, 100, 11, 3]), 'No')


if __name__ == '__main__':
    unittest.main()
