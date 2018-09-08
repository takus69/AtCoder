import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3), 2)
        self.assertEqual(run(6), 9)
        self.assertEqual(run(11), 30)
        self.assertEqual(run(50), 625)


if __name__ == '__main__':
    unittest.main()
