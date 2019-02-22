import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 5, [10, 12, 1, 2, 14]), 5)
        self.assertEqual(run(3, 7, [-10, -3, 0, 9, -100, 2, 17]), 19)
        self.assertEqual(run(100, 1, [-100000]), 0)


if __name__ == '__main__':
    unittest.main()
