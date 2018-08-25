import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [10, 30, 20]), 30)
        self.assertEqual(run(4, [10, 30, 20, 40]), 30)


if __name__ == '__main__':
    unittest.main()
