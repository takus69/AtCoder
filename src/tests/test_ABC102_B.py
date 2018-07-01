import unittest

from app.ABC102_B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, [1, 4, 6, 3]), 5)
        self.assertEqual(run(2, [1000000000, 1]), 999999999)
        self.assertEqual(run(5, [1, 1, 1, 1, 1]), 0)


if __name__ == '__main__':
    unittest.main()
