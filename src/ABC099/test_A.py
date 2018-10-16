import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(999), 'ABC')
        self.assertEqual(run(1000), 'ABD')
        self.assertEqual(run(1481), 'ABD')


if __name__ == '__main__':
    unittest.main()
