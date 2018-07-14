import unittest

from app.AGC026_A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, [1, 1, 2, 2, 2]), 2)
        self.assertEqual(run(3, [1, 2, 1]), 0)
        self.assertEqual(run(5, [1, 1, 1, 1, 1]), 2)
        self.assertEqual(run(14, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4]),
                         4)


if __name__ == '__main__':
    unittest.main()
