import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 4, 2), '5 3')
        self.assertEqual(run(3, 3, 3), '1 3')
        self.assertEqual(run(314159265, 358979323, 84), '448759046 224379523')


if __name__ == '__main__':
    unittest.main()
