import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 1), 'Yes')
        self.assertEqual(run(1, 2), 'No')


if __name__ == '__main__':
    unittest.main()
