import unittest

from app.ABC102_D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, [3, 2, 4, 1, 2]), 2)
        self.assertEqual(run(10, [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]), 36)
        self.assertEqual(run(7, [1, 2, 3, 1000000000, 4, 5, 6]), 999999994)


if __name__ == '__main__':
    unittest.main()
