import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(1, 3, 2), 1)
        self.assertEqual(run(1, 3, 1), 2)
        self.assertEqual(run(2, 3, 3), 1)
        self.assertEqual(run(2, 3, 1), 5)
        self.assertEqual(run(7, 1, 1), 1)
        self.assertEqual(run(15, 8, 5), 437760187)


if __name__ == '__main__':
    unittest.main()
