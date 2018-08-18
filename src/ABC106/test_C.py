import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('1214', 4), 2)
        self.assertEqual(run('3', 157), 3)
        self.assertEqual(run('299792458', 9460730472580800), 2)


if __name__ == '__main__':
    unittest.main()
