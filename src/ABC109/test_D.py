import unittest

from D import run


@unittest.skip('Many answers')
class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2, 3, [[1, 2, 3], [0, 1, 1]]),
                         [3, [[2, 2, 2, 3], [1, 1, 1, 2], [1, 3, 1, 2]]])


if __name__ == '__main__':
    unittest.main()
