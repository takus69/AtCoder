import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(8, 9, [[0, 1, 2], [0, 3, 2],
                             [1, 1, 3], [1, 1, 4], [0, 2, 4],
                             [1, 4, 1], [0, 4, 2], [0, 0, 0],
                             [1, 0, 0]]), ['Yes', 'No', 'Yes', 'Yes'])


if __name__ == '__main__':
    unittest.main()
