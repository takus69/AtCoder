import unittest

from app.ABC103_D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 2, [[1, 4], [2, 5]]), 1)
        self.assertEqual(run(9, 5, [[1, 8], [2, 7], [3, 5],
                         [4, 6], [7, 9]]), 2)
        self.assertEqual(run(5, 10, [[1, 2], [1, 3], [1, 4], [1, 5],
                         [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]), 4)


if __name__ == '__main__':
    unittest.main()
