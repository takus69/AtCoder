import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(1, 5, 2), 53)
        self.assertEqual(run(9, 9, 9), 108)
        self.assertEqual(run(6, 6, 7), 82)


if __name__ == '__main__':
    unittest.main()
