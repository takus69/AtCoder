import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(0, 0), 0)
        self.assertEqual(run(0, 1), 1)
        self.assertEqual(run(1, 0), 0)
        self.assertEqual(run(1, 1), 0)
        self.assertEqual(run(1, 2), 1)
        self.assertEqual(run(1, 3), 2)
        self.assertEqual(run(1, 4), 3)
        self.assertEqual(run(1, 5), 3)
        self.assertEqual(run(2, 7), 4)
        self.assertEqual(run(1, 1), 0)
        self.assertEqual(run(50, 4321098765432109), 2160549382716056)


if __name__ == '__main__':
    unittest.main()
