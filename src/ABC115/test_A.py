import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(25), 'Christmas')
        self.assertEqual(run(24), 'Christmas Eve')
        self.assertEqual(run(23), 'Christmas Eve Eve')
        self.assertEqual(run(22), 'Christmas Eve Eve Eve')


if __name__ == '__main__':
    unittest.main()
