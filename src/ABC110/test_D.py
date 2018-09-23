import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 6), 4)
        self.assertEqual(run(3, 12), 18)
        self.assertEqual(run(100000, 1000000000), 957870001)


if __name__ == '__main__':
    unittest.main()
