import unittest

from app.ABC100_C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        n = 3
        a = [5, 2, 4]
        self.assertEqual(run(n, a), 3)

        n = 4
        a = [631, 577, 243, 199]
        self.assertEqual(run(n, a), 0)

        n = 10
        a = [2184, 2126, 1721, 1800, 1024,
             2528, 3360, 1945, 1280, 1776]
        self.assertEqual(run(n, a), 39)


if __name__ == '__main__':
    unittest.main()
