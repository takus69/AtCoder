import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2750, 628), 'W 5')
        self.assertEqual(run(161, 8), 'C 0')
        self.assertEqual(run(3263, 15), 'NNW 1')
        self.assertEqual(run(1462, 1959), 'SE 12')
        self.assertEqual(run(1687, 1029), 'SSE 8')
        self.assertEqual(run(2587, 644), 'WSW 5')
        self.assertEqual(run(113, 201), 'NNE 3')
        self.assertEqual(run(2048, 16), 'SSW 1')


if __name__ == '__main__':
    unittest.main()
