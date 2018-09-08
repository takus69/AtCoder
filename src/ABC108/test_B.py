import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(0, 0, 0, 1), '-1 1 -1 0')
        self.assertEqual(run(2, 3, 6, 6), '3 10 -1 7')
        self.assertEqual(run(31, -41, -59, 26), '-126 -64 -36 -131')


if __name__ == '__main__':
    unittest.main()
