import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(9), 0)
        self.assertEqual(run(10), 1)
        self.assertEqual(run(100), 543)


if __name__ == '__main__':
    unittest.main()
