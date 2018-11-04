import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(81, 58), 110)
        self.assertEqual(run(4, 54), 31)


if __name__ == '__main__':
    unittest.main()
