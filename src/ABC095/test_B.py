import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 1000, [120, 100, 140]), 9)
        self.assertEqual(run(4, 360, [90, 90, 90, 90]), 4)
        self.assertEqual(run(5, 3000, [150, 130, 150, 130, 110]), 26)


if __name__ == '__main__':
    unittest.main()
