import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(575), 4)
        self.assertEqual(run(3600), 13)
        self.assertEqual(run(999999999), 26484)


if __name__ == '__main__':
    unittest.main()
