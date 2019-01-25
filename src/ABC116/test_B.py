import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(8), 5)
        self.assertEqual(run(7), 18)
        self.assertEqual(run(54), 114)


if __name__ == '__main__':
    unittest.main()
