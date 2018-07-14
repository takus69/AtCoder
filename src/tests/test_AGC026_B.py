import unittest

from app.AGC026_B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, [9, 9], [7, 7], [5, 6], [9, 9]), ['No', 'Yes'])
        self.assertEqual(run(2, [14, 14], [10, 10], [7, 8], [12, 12]),
                         ['No', 'Yes'])
        self.assertEqual(run(2, [14, 14], [10, 10], [9, 7], [12, 11]),
                         ['Yes', 'No'])


if __name__ == '__main__':
    unittest.main()
