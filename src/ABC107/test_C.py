import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 3, [-30, -10, 10, 20, 50]), 40)
        self.assertEqual(run(3, 2, [10, 20, 30]), 20)
        self.assertEqual(run(1, 1, [0]), 0)
        self.assertEqual(run(8, 5, [-9, -7, -4, -3, 1, 2, 3, 4]), 10)
        self.assertEqual(run(5, 3, [-30, -10, 20, 30, 50]), 50)
        self.assertEqual(run(5, 5, [-30, -10, 20, 30, 50]), 110)
        self.assertEqual(run(5, 3, [-30, -20, 10, 30, 50]), 50)


if __name__ == '__main__':
    unittest.main()
