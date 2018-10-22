import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(6, 'aabbca'), 2)
        self.assertEqual(run(10, 'aaaaaaaaaa'), 1)
        self.assertEqual(run(45, 'tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir'), 9)


if __name__ == '__main__':
    unittest.main()
