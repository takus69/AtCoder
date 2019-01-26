import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 3, [1, 1, 2, 2, 3], [9, 7, 6, 5, 1]), 26)
        self.assertEqual(run(7, 4, [1, 2, 3, 4, 4, 4, 4],
                         [1, 1, 1, 6, 5, 5, 5]), 25)
        self.assertEqual(run(6, 5, [5, 2, 3, 6, 6, 4],
                         [1000000000, 990000000, 980000000,
                          970000000, 960000000, 950000000]), 4900000016)


if __name__ == '__main__':
    unittest.main()
