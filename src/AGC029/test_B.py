import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [1, 2, 3]), 1)
        self.assertEqual(run(5, [3, 11, 14, 5, 13]), 2)


if __name__ == '__main__':
    unittest.main()
