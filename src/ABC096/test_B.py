import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 3, 11, 1), 30)
        self.assertEqual(run(3, 3, 4, 2), 22)


if __name__ == '__main__':
    unittest.main()
