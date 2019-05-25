import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 7, [1, 6, 3]), 14)
        self.assertEqual(run(4, 9, [7, 4, 0, 3]), 46)
        self.assertEqual(run(1, 0, [1000000000000]), 1000000000000)


if __name__ == '__main__':
    unittest.main()
