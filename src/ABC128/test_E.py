import unittest

from E import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 6, [[1, 3, 2], [7, 13, 10], [18, 20, 13], [3, 4, 2]], [8]), [2, 2, 10, -1, 13, -1])


if __name__ == '__main__':
    unittest.main()
