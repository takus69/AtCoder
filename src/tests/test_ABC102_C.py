import unittest

from app.ABC102_C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, [2, 2, 3, 5, 5]), 2)
        self.assertEqual(run(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)
        self.assertEqual(run(6, [6, 5, 4, 3, 2, 1]), 18)
        self.assertEqual(run(7, [1, 1, 1, 1, 2, 3, 4]), 6)
        self.assertEqual(run(4, [2, 4, 8, 11]), 9)


if __name__ == '__main__':
    unittest.main()
