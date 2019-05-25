import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 1, [(1, 2), (1, 3), (2, 3)]), [0, 1, 2])
        self.assertEqual(run(6, 3, [(2, 1), (2, 3), (4, 1), (4, 2), (6, 1), (2, 6), (4, 6), (6, 5)]), [6, 4, 2, 0, 6, 2])


if __name__ == '__main__':
    unittest.main()
