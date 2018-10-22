import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 'WEEWW'), 1)
        self.assertEqual(run(12, 'WEWEWEEEWWWE'), 4)
        self.assertEqual(run(8, 'WWWWWEEE'), 3)


if __name__ == '__main__':
    unittest.main()
