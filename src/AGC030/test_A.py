import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 1, 4), 5)
        self.assertEqual(run(5, 2, 9), 10)
        self.assertEqual(run(8, 8, 1), 9)


if __name__ == '__main__':
    unittest.main()
