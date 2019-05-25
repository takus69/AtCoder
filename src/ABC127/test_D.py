import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 2, [5, 1, 4], {3: 2, 5: 1}), 14)
        self.assertEqual(run(10, 3, [1, 8, 5, 7, 100, 4, 52, 33, 13, 5], {10: 3, 30: 4, 4: 1}), 338)
        self.assertEqual(run(3, 2, [100, 100, 100], {99: 6}), 300)
        self.assertEqual(run(11, 3, [1]*11, {1000000000: 10}), 10000000001)


if __name__ == '__main__':
    unittest.main()
