import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, [6, 8, 1, 2, 3]), 21)
        self.assertEqual(run(6, [3, 1, 4, 1, 5, 9]), 25)
        self.assertEqual(run(3, [5, 5, 1]), 8)



if __name__ == '__main__':
    unittest.main()
