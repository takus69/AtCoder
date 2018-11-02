import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(1500, 2000, 1600, 3, 2), 7900)
        self.assertEqual(run(1500, 2000, 1900, 3, 2), 8500)
        self.assertEqual(run(1500, 2000, 500, 90000, 100000), 100000000)


if __name__ == '__main__':
    unittest.main()
