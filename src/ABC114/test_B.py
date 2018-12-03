import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(1234567876), 34)
        self.assertEqual(run(35753), 0)
        self.assertEqual(run(1111111111), 642)


if __name__ == '__main__':
    unittest.main()
