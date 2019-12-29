import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5, 2, 8, 7, 6, 'rsrpr'), 27)
        self.assertEqual(run(7, 1, 100, 10, 1, 'ssssppr'), 211)
        self.assertEqual(run(30, 5, 325, 234, 123, 'rspsspspsrpspsppprpsprpssprpsr'), 4996)


if __name__ == '__main__':
    unittest.main()
