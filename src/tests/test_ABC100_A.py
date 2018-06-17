import unittest

from app.ABC100_A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 4), 'Yay!')
        self.assertEqual(run(11, 4), ':(')


if __name__ == '__main__':
    unittest.main()
