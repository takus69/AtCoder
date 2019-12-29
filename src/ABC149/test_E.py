import unittest

from E import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 3, [10, 14, 19, 34, 33]), 202)
        self.assertEqual(run(9, 14, [1, 3, 5, 110, 24, 21, 34, 5, 3]), 1837)
        self.assertEqual(run(9, 73, [67597, 52981, 5828, 66249, 75177, 64141, 40773, 79105, 16076]), 8128170)


if __name__ == '__main__':
    unittest.main()
