import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 2, 10, 20, [8, 15, 13], [16, 22]), 'No War')
        self.assertEqual(run(4, 2, -48, -1, [-20, -35, -91, -23], [-22, 66]),
                         'War')
        self.assertEqual(run(5, 3, 6, 8, [-10, 3, 1, 5, -100], [100, 6, 14]),
                         'War')


if __name__ == '__main__':
    unittest.main()
