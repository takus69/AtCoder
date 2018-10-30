import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5), '3 5 7 11 31')
        self.assertEqual(run(6), '2 3 5 7 11 13')
        self.assertEqual(run(7), '2 5 7 13 19 37 67 79')


if __name__ == '__main__':
    unittest.main()
