import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 2), 1)
        self.assertEqual(run(5, 7), 24)


if __name__ == '__main__':
    unittest.main()
