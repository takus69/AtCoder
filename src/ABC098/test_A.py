import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 1), 4)
        self.assertEqual(run(4, -2), 6)
        self.assertEqual(run(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
