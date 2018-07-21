import unittest

from app.ABC103_A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run([1, 6, 3]), 5)
        self.assertEqual(run([11, 5, 5]), 6)
        self.assertEqual(run([100, 100, 100]), 0)


if __name__ == '__main__':
    unittest.main()
