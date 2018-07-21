import unittest

from app.ABC103_D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 2, [[1, 4], [2, 5]]), 1)
        self.assertEqual(run(9, 5, [[1, 8], [2, 7], [3, 5],
                         [4, 6], [7, 9]]), 2)


if __name__ == '__main__':
    unittest.main()
