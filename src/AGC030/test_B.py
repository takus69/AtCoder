import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(10, 3, [2, 7, 9]), 15)
        self.assertEqual(run(10, 6, [1, 2, 3, 6, 7, 9]), 27)
        self.assertEqual(run(314159265, 7, [
            21662711, 77271666, 89022761, 156626166,
            160332356, 166902656, 298992265]), 1204124749)


if __name__ == '__main__':
    unittest.main()
