import unittest

from D import run
import D


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 2, [1, 2, 3], [[1, 2], [1, 3]]), 6)
        self.assertEqual(run(5, 3, [3, 2, 3, 1, 4], [[1, 5], [2, 3], [4, 2]]),
                         36)
        self.assertEqual(run(9, 5, [3, 1, 4, 1, 5, 9, 2, 6, 5],
                         [[3, 5], [8, 9], [7, 9], [3, 2], [3, 8]]), 425)

    def test_count_swap(self):
        self.assertEqual(D.count_swap([1, 2, 3]), 0)
        self.assertEqual(D.count_swap([1, 3, 2]), 1)
        self.assertEqual(D.count_swap([3, 2, 1]), 3)
        self.assertEqual(D.count_swap([2, 3, 1]), 2)

    def test_swap(self):
        A = [1, 2, 3]
        self.assertEqual(A, [1, 2, 3])
        self.assertEqual(D.swap(A, [1, 2]), [2, 1, 3])
        self.assertEqual(A, [1, 2, 3])
        self.assertEqual(D.swap(A, [1, 3]), [3, 2, 1])
        self.assertEqual(A, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
