import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('BBW'), 2)
        self.assertEqual(run('BWBWBW'), 6)


if __name__ == '__main__':
    unittest.main()
