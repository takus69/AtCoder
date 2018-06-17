import unittest

from app.ABC100_D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        n = 5
        m = 3
        x = [3, 1, 2, 3, 9]
        y = [1, 5, 6, 5, 7]
        z = [4, 9, 5, 8, 9]
        self.assertEqual(run(n, m, x, y, z), 56)

        n = 5
        m = 3
        x = [1, -4, 7, -10, 13]
        y = [-2, 5, -8, 11, -14]
        z = [3, -6, -9, -12, 15]
        # self.assertEqual(run(n, m, x, y, z), 54)


if __name__ == '__main__':
    unittest.main()
