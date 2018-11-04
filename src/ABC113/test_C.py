import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 3, [[1, 32, 0], [2, 63, 1], [1, 12, 2]]),
                         ['000001000002', '000002000001', '000001000001'])
        self.assertEqual(run(2, 3, [[2, 55, 0], [2, 77, 1], [2, 99, 2]]),
                         ['000002000001', '000002000002', '000002000003'])


if __name__ == '__main__':
    unittest.main()
