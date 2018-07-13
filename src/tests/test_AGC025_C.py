import unittest

from app.AGC025_C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [-5, 3, -4], [1, 7, -2]), 10)
        self.assertEqual(run(3, [1, 3, 5], [2, 4, 6]), 12)
        self.assertEqual(run(5, [-2, -2, 7, 9, -2], [0, 0, 8, 10, -1]),
                         34)


if __name__ == '__main__':
    unittest.main()
