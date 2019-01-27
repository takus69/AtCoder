import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(10, 3, 5), '3 0')
        self.assertEqual(run(10, 7, 5), '5 2')
        self.assertEqual(run(100, 100, 100), '100 100')


if __name__ == '__main__':
    unittest.main()
