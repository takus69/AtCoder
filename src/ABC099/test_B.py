import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(8, 13), 2)
        self.assertEqual(run(54, 65), 1)


if __name__ == '__main__':
    unittest.main()
