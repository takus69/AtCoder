import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 2), 3)
        self.assertEqual(run(1, 1), 1)
        self.assertEqual(run(15, 11), 5)


if __name__ == '__main__':
    unittest.main()
