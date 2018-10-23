import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, [2, 5, 4, 6]), 5)
        self.assertEqual(run(9, [0]*9), 45)
        self.assertEqual(run(19, [885, 8, 1, 128, 83, 32, 256, 206, 639, 16, 4, 128, 689, 32, 8, 64, 885, 969, 1]), 37)


if __name__ == '__main__':
    unittest.main()
