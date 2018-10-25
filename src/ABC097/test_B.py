import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(10), 9)
        self.assertEqual(run(1), 1)
        self.assertEqual(run(999), 961)


if __name__ == '__main__':
    unittest.main()
