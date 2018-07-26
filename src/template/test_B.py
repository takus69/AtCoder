import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(0, 5), 5)
        self.assertEqual(run(1, 11), 1100)
        self.assertEqual(run(2, 85), 850000)
        self.assertEqual(run(0, 100), 101)
        self.assertEqual(run(1, 100), 10100)


if __name__ == '__main__':
    unittest.main()
