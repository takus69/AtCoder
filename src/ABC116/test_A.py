import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run([3, 4, 5]), 6)
        self.assertEqual(run([5, 12, 13]), 30)
        self.assertEqual(run([45, 28, 53]), 630)


if __name__ == '__main__':
    unittest.main()
