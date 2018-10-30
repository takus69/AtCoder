import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 5), 5)
        self.assertEqual(run(2, 1), 1)
        self.assertEqual(run(11, 30), 11)


if __name__ == '__main__':
    unittest.main()
