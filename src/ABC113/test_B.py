import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 12, 5, [1000, 2000]), 1)
        self.assertEqual(run(3, 21, -11, [81234, 94124, 52141]), 3)


if __name__ == '__main__':
    unittest.main()
