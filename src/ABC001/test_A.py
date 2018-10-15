import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(15, 10), 5)
        self.assertEqual(run(0, 0), 0)
        self.assertEqual(run(5, 20), -15)


if __name__ == '__main__':
    unittest.main()
