import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 100, [1, 10]), 355)
        self.assertEqual(run(5, 1, [1, 999999997, 999999998, 999999999,
                             1000000000]), 19999999983)
        self.assertEqual(run(10, 8851025, [38, 87, 668, 3175, 22601,
                         65499, 90236, 790604, 4290609, 4894746]), 150710136)
        self.assertEqual(run(16, 10, [1, 7, 12, 27, 52, 75, 731, 13856,
                             395504, 534840, 1276551, 2356789, 9384806,
                             19108104, 82684732, 535447408]), 3256017715)


if __name__ == '__main__':
    unittest.main()
