import unittest

from app.ABC102_D import run, calc_sum, target_sp


class TestSample(unittest.TestCase):
    def test_run(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        sp = [2, 3, 5]
        self.assertEqual(calc_sum(a, sp), (3, 3, 9, 13))

        n = 4
        sp = [1, 2, 3]
        self.assertEqual(target_sp(sp, n), [])
        n = 5
        sp = [1, 2, 4]
        self.assertEqual(target_sp(sp, n), [2])

        self.assertEqual(run(5, [3, 2, 4, 1, 2]), 2)
        self.assertEqual(run(10, [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]), 36)
        self.assertEqual(run(7, [1, 2, 3, 1000000000, 4, 5, 6]), 999999994)


if __name__ == '__main__':
    unittest.main()
