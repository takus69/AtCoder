import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 7, 9, 3), 'Yes')
        self.assertEqual(run(100, 10, 1, 2), 'No')
        self.assertEqual(run(10, 10, 10, 1), 'Yes')
        self.assertEqual(run(1, 100, 2, 10), 'Yes')


if __name__ == '__main__':
    unittest.main()
