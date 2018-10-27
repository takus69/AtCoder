import unittest

from D import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3), ['Yes', 3, [[2, 1, 2], [2, 1, 3], [2, 2, 3]]])
        self.assertEqual(run(4), ['No'])


if __name__ == '__main__':
    unittest.main()
