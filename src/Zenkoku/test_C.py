import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [10, 20, 30], [10, 20, 30]), 20)
        self.assertEqual(run(3, [20, 20, 20], [10, 20, 30]), 20)
        self.assertEqual(run(6, [1]*6, [1000000000]*6), -2999999997)


if __name__ == '__main__':
    unittest.main()
