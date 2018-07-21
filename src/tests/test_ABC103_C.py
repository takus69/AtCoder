import unittest

from app.ABC103_C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [3, 4, 6]), 10)
        self.assertEqual(run(5, [7, 46, 11, 20, 11]), 90)
        self.assertEqual(run(7, [994, 518, 941, 851, 647, 2, 581]), 4527)


if __name__ == '__main__':
    unittest.main()
