import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertAlmostEqual(run(8, 3), 2.6666666667, 4)
        self.assertAlmostEqual(run(99, 1), 99.0000000000, 4)
        self.assertAlmostEqual(run(1, 100), 0.0100000000, 4)


if __name__ == '__main__':
    unittest.main()
